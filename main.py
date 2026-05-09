from PyQt5.QtWidgets import QApplication, QWidget
import sys

app = QApplication(sys.argv)

window = QWidget()
window.resize(800, 600)
window.setWindowTitle("2D Geometry Editor")

window.show()

sys.exit(app.exec_())