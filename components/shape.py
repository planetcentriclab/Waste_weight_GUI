from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Rectangle(QWidget):  
    """
    A class representing a rectangular shape.

    This class inherits from QWidget.

    Attributes:
        line_color (QColor): Color for the border of the rectangle.
        background_color (QColor): Background color of the rectangle.
        x (int): X-coordinate position of the top-left corner of the rectangle.
        y (int): Y-coordinate position of the top-left corner of the rectangle.
        w (int): Width of the rectangle.
        h (int): Height of the rectangle.
        x_radius (int): X-axis radius for rounding the corners of the rectangle.
        y_radius (int): Y-axis radius for rounding the corners of the rectangle.

    Methods:
        __init__: Initializes the Rectangle object with provided parameters.
    """
    def __init__(self, painter, line_color, background_color, x, y, w, h, x_radius, y_radius):
        super().__init__()  # Call the superclass constructor
        self.line_color = line_color
        self.background_color = background_color
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.x_radius = x_radius
        self.y_radius = y_radius
        painter.setPen(QPen(self.line_color))
        painter.setBrush(QBrush(self.background_color, Qt.SolidPattern))
        painter.drawRoundedRect(self.x, self.y, self.w, self.h, self.x_radius, self.y_radius)

class Line():
    """
    A class representing a line.

    Attributes:
        line_color (QColor): Color for the line.
        x1 (int): X-coordinate position of the start point of the line.
        y1 (int): Y-coordinate position of the start point of the line.
        x2 (int): X-coordinate position of the end point of the line.
        y2 (int): Y-coordinate position of the end point of the line.

    Methods:
        __init__: Initializes the Line object with provided parameters.
    """
    def __init__(self, painter, line_color, x1, y1, x2, y2):
        super().__init__()  # Call the superclass constructor
        self.line_color = line_color
        painter.setPen(QPen(self.line_color))
        painter.drawLine(x1, y1, x2, y2)