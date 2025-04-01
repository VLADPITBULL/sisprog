from PyQt5.QtWidgets import QApplication
from views import MaterialWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MaterialWindow()
    window.show()
    sys.exit(app.exec_())
