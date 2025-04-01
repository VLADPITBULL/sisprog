from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QListWidgetItem, QLineEdit
from controllers import get_all_materials

class MaterialWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Материалы")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Поиск по названию...")
        self.search_bar.textChanged.connect(self.update_list)

        self.list_widget = QListWidget()
        layout.addWidget(self.search_bar)
        layout.addWidget(self.list_widget)

        self.setLayout(layout)
        self.update_list()

    def update_list(self):
        search = self.search_bar.text().lower()
        self.list_widget.clear()
        materials = get_all_materials()
        for mat in materials:
            if search in mat.name.lower():
                item = QListWidgetItem(f"{mat.type} | {mat.name}\n"
                                       f"Минимум: {mat.min_stock} {mat.unit} | Остаток: {mat.stock_qty} {mat.unit}\n"
                                       f"Поставщики: {', '.join([s.name for s in mat.suppliers])}")
                self.list_widget.addItem(item)
