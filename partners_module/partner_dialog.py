from PyQt5.QtWidgets import QDialog, QFormLayout, QLineEdit, QPushButton

class PartnerDialog(QDialog):
    def __init__(self, data=None):
        super().__init__()
        self.setWindowTitle("Партнёр")
        self.fields = {}
        layout = QFormLayout()

        for field in ["company_name", "type", "inn", "kpp", "director_name", "contact_phone", "contact_email", "priority"]:
            inp = QLineEdit()
            if data and field in data:
                inp.setText(str(data[field]))
            self.fields[field] = inp
            layout.addRow(field.replace("_", " ").title(), inp)

        self.save_btn = QPushButton("Сохранить")
        self.save_btn.clicked.connect(self.accept)
        layout.addRow(self.save_btn)
        self.setLayout(layout)

    def get_data(self):
        return {k: v.text() for k, v in self.fields.items()}
