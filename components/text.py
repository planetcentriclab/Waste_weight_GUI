from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Text():
    """
    A class representing a text label.

    Attributes:
        window (QWidget): The parent widget to which the text label belongs.
        text (str): The text content of the label.
        font_name (str): The font name of the text.
        font_size (int): The font size of the text.
        pos_x (int): The x-coordinate position of the text label.
        pos_y (int): The y-coordinate position of the text label.
        size_x (int): The width of the text label.
        size_y (int): The height of the text label.
        style (str): The style sheet for the text label.
        alignment (Qt.AlignmentFlag): The alignment of the text label.

    Methods:
        __init__: Initializes the Text object with provided parameters.
        set_text: Sets the text content of the label.
        show: Makes the text label visible.
        hide: Hides the text label.
    """
    def __init__(self, window, text, font_name, font_size, pos_x, pos_y, size_x, size_y, style, alignment=None):
        self.window = window
        self.font_name = font_name
        self.font_size = font_size
        self.object = QLabel(window)
        self.object.setText(text)
        self.object.setFont(QFont(font_name, font_size))
        self.object.resize(size_x, size_y)
        self.object.move(pos_x, pos_y)
        self.object.setStyleSheet(style)
        self.object.setAlignment(alignment)
    
    def set_text(self, text):
        """
        Function to set the text content of the label.

        Args:
            text (str): The new text content.
        """
        self.object.setText(text)
        self.object.setFont(QFont(self.font_name, self.font_size))

    def show(self):
        self.object.setVisible(True)
    
    def hide(self):
        self.object.setVisible(False)
    