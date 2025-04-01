from PyQt5.QtWidgets import QApplication
from views import PartnerWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PartnerWindow()
    window.show()
    sys.exit(app.exec_())
