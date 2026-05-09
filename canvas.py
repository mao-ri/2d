from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt

from point import Point
from line import Line


class Canvas(QWidget):

    def __init__(self):
        super().__init__()

        self.points = []
        self.lines = []

        self.selected_point = None

        self.setMinimumSize(800, 600)

    def mousePressEvent(self, event):

        x = event.x()
        y = event.y()

        point = Point(x, y)

        self.points.append(point)

        # 第一次点击
        if self.selected_point is None:

            self.selected_point = point

        # 第二次点击
        else:

            line = Line(self.selected_point, point)

            self.lines.append(line)

            self.selected_point = None

        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(QPainter.Antialiasing)

        # 画线
        painter.setPen(Qt.black)

        for line in self.lines:

            painter.drawLine(
                line.start.x,
                line.start.y,
                line.end.x,
                line.end.y
            )

        # 画点
        painter.setBrush(Qt.black)

        for point in self.points:

            painter.drawEllipse(
                point.x - 4,
                point.y - 4,
                8,
                8
            )