from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton
)

from canvas import Canvas



class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("2D Geometry Editor")
        self.resize(800, 600)

        self.canvas = Canvas()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)

        # ===== 按钮栏 =====
        button_layout = QHBoxLayout()

        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.clear_canvas)

        save_button = QPushButton("Save")
        save_button.clicked.connect(self.canvas.save_to_json)

        button_layout.addWidget(clear_button)
        button_layout.addWidget(save_button)

        # ⚠️关键：把按钮容器放入一个 QWidget（避免被挤没）
        button_widget = QWidget()
        button_widget.setLayout(button_layout)

        main_layout.addWidget(button_widget)

        # 画布
        main_layout.addWidget(self.canvas)

    def clear_canvas(self):
        self.canvas.points.clear()
        self.canvas.lines.clear()
        self.canvas.update()
