import sys

from PyQt5.QtWidgets import QApplication

from canvas import Canvas


app = QApplication(sys.argv)

window = Canvas()

window.setWindowTitle("2D Geometry Editor")

window.show()

sys.exit(app.exec_())