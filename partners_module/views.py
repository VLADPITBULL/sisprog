from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox, QLabel
from partner_dialog import PartnerDialog
from controllers import get_partners, create_partner, update_partner, delete_partner

class PartnerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Партнёры")
        self.resize(1000, 600)

        self.page = 1
        self.per_page = 10

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        btn_layout = QHBoxLayout()
        self.prev_btn = QPushButton("← Назад")
        self.next_btn = QPushButton("Вперёд →")
        self.add_btn = QPushButton("Добавить")
        self.edit_btn = QPushButton("Редактировать")
        self.del_btn = QPushButton("Удалить")
        self.page_label = QLabel()

        self.prev_btn.clicked.connect(self.prev_page)
        self.next_btn.clicked.connect(self.next_page)
        self.add_btn.clicked.connect(self.add_partner)
        self.edit_btn.clicked.connect(self.edit_partner)
        self.del_btn.clicked.connect(self.delete_partner)

        btn_layout.addWidget(self.prev_btn)
        btn_layout.addWidget(self.next_btn)
        btn_layout.addWidget(self.page_label)
        btn_layout.addStretch()
        btn_layout.addWidget(self.add_btn)
        btn_layout.addWidget(self.edit_btn)
        btn_layout.addWidget(self.del_btn)

        self.layout.addLayout(btn_layout)
        self.load_partners()

    def load_partners(self):
        self.table.clear()
        partners, total = get_partners(self.page, self.per_page)
        self.page_label.setText(f"Стр. {self.page} из {((total-1)//self.per_page)+1}")
        self.table.setRowCount(len(partners))
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID", "Компания", "ИНН", "Email", "Приоритет"])
        for i, p in enumerate(partners):
            self.table.setItem(i, 0, QTableWidgetItem(str(p.id)))
            self.table.setItem(i, 1, QTableWidgetItem(p.company_name))
            self.table.setItem(i, 2, QTableWidgetItem(p.inn))
            self.table.setItem(i, 3, QTableWidgetItem(p.contact_email))
            self.table.setItem(i, 4, QTableWidgetItem(str(p.priority)))

    def prev_page(self):
        if self.page > 1:
            self.page -= 1
            self.load_partners()

    def next_page(self):
        self.page += 1
        self.load_partners()

    def add_partner(self):
        dlg = PartnerDialog()
        if dlg.exec_():
            create_partner(dlg.get_data())
            self.load_partners()

    def edit_partner(self):
        row = self.table.currentRow()
        if row < 0: return
        partner_id = int(self.table.item(row, 0).text())
        data = {
            "company_name": self.table.item(row, 1).text(),
            "inn": self.table.item(row, 2).text(),
            "contact_email": self.table.item(row, 3).text(),
            "priority": self.table.item(row, 4).text()
        }
        dlg = PartnerDialog(data)
        if dlg.exec_():
            update_partner(partner_id, dlg.get_data())
            self.load_partners()

    def delete_partner(self):
        row = self.table.currentRow()
        if row < 0: return
        partner_id = int(self.table.item(row, 0).text())
        reply = QMessageBox.question(self, "Удаление", "Удалить партнёра?")
        if reply == QMessageBox.Yes:
            delete_partner(partner_id)
            self.load_partners()
