from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
import math
import json

from point import Point
from line import Line
from PyQt5.QtGui import QPainter, QPainterPath
from curve import Curve



class Canvas(QWidget):

    def __init__(self):
        self.dragging_point = None
        super().__init__()

        self.points = []
        self.lines = []
        self.curves = []
        self.temp_points = []

        self.selected_point = None

        self.setMinimumSize(800, 600)

    def mousePressEvent(self, event):

        x = event.x()
        y = event.y()

        # =========================
        # 右键删除线
        # =========================
        if event.button() == Qt.RightButton:

            for line in self.lines:

                distance = self.point_to_line_distance(
                    x, y,
                    line.start.x, line.start.y,
                    line.end.x, line.end.y
                )

                if distance < 8:

                    self.lines.remove(line)
                    self.update()
                    return

        # =========================
        # 左键逻辑
        # =========================
        if event.button() == Qt.LeftButton:

            clicked_point = self.find_point(x, y)

            # =====================
            # ⭐ 1. 点在已有点上
            # =====================
            if clicked_point:

                # ---------- 曲线逻辑 ----------
                self.temp_points.append(clicked_point)

                if len(self.temp_points) == 3:

                    curve = Curve(
                        self.temp_points[0],
                        self.temp_points[1],
                        self.temp_points[2]
                    )

                    self.curves.append(curve)
                    self.temp_points = []

                # ---------- 拖拽 ----------
                self.dragging_point = clicked_point

                # ---------- 连线 ----------
                if self.selected_point is None:

                    self.selected_point = clicked_point

                else:

                    if clicked_point != self.selected_point:

                        line = Line(
                            self.selected_point,
                            clicked_point
                        )

                        self.lines.append(line)

                    self.selected_point = None

            # =====================
            # ⭐ 2. 空白区域：创建点
            # =====================
            else:

                point = Point(x, y)
                self.points.append(point)

            self.update()
    def point_to_line_distance(self, px, py, x1, y1, x2, y2):

        dx = x2 - x1
        dy = y2 - y1

        if dx == 0 and dy == 0:
            return math.hypot(px - x1, py - y1)

        t = ((px - x1) * dx + (py - y1) * dy) / (dx * dx + dy * dy)

        t = max(0, min(1, t))

        nearest_x = x1 + t * dx
        nearest_y = y1 + t * dy

        return math.hypot(px - nearest_x, py - nearest_y)
    
    def find_point(self, x, y):

        for point in self.points:

            distance = math.hypot(
                point.x - x,
                point.y - y
            )

            if distance < 8:
                return point

        return None

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(QPainter.Antialiasing)

        # ====================
        # 画网格
        # ====================

        painter.setPen(Qt.lightGray)

        grid_size = 25

        width = self.width()
        height = self.height()

        # 竖线
        for x in range(0, width, grid_size):

            painter.drawLine(
                x,
                0,
                x,
                height
            )

        # 横线
        for y in range(0, height, grid_size):

            painter.drawLine(
                0,
                y,
                width,
                y
            )

        # ====================
        # 画线
        # ====================

        painter.setPen(Qt.black)

        for line in self.lines:

            painter.drawLine(
                line.start.x,
                line.start.y,
                line.end.x,
                line.end.y
            )


        painter.setPen(Qt.blue)

        for curve in self.curves:

            path = QPainterPath()
            path.moveTo(curve.start.x, curve.start.y)

            path.quadTo(
                curve.control.x, curve.control.y,
                curve.end.x, curve.end.y
            )

            painter.drawPath(path)
        # ====================
        # 画点
        # ====================

        for point in self.points:

            # 选中点：红色
            if point == self.selected_point:

                painter.setBrush(Qt.red)

            else:

                painter.setBrush(Qt.black)

            painter.drawEllipse(
                point.x - 4,
                point.y - 4,
                8,
                8
            )


    def save_to_json(self):

        data = {
            "points": [],
            "lines": []
        }

        # 保存点
        for point in self.points:

            data["points"].append({
                "x": point.x,
                "y": point.y
            })

        # 保存线
        for line in self.lines:

            start_index = self.points.index(line.start)
            end_index = self.points.index(line.end)

            data["lines"].append({
                "start": start_index,
                "end": end_index
            })

        with open("scene.json", "w") as file:

            json.dump(
                data,
                file,
                indent=4
            )

        print("Saved to scene.json")
            


    def mouseMoveEvent(self, event):

        if self.dragging_point:

            self.dragging_point.x = event.x()
            self.dragging_point.y = event.y()

            self.update()


    def mouseReleaseEvent(self, event):

        self.dragging_point = None
