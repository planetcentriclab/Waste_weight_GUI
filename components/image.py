from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Image(QLabel):
    """
    A class representing an image displayed within a QLabel.

    Methods:
        __init__: Initializes the Image object with the provided image path, position, width, and height.
    """

    def __init__(self, window, image_path, pos_x, pos_y, w, h):
        """
        Initializes the Image object with the provided parameters.

        Args:
            window: Parent widget.
            image_path (str): Path to the image file.
            pos_x (int): The X-coordinate of the image position.
            pos_y (int): The Y-coordinate of the image position.
            w (int): The width of the image.
            h (int): The height of the image.
        """
        super().__init__(window)
        scale = QSize(w, h)
        pixmap = QPixmap(image_path)
        self.setPixmap(pixmap.scaled(scale))
        self.setStyleSheet("background-color: transparent;")
        self.resize(w, h)
        self.move(pos_x, pos_y)

class ImageButton(QLabel):
    """
    A class representing an image button that emits a signal upon click.

    Attributes:
        clicked (pyqtSignal): Signal emitted when the image button is clicked.

    Methods:
        __init__: Initializes the ImageButton object with the provided image path, position, width, and height.
        mousePressEvent: Overrides the mouse press event to emit the clicked signal upon image button click.
    """

    clicked = pyqtSignal()
    def __init__(self, window, image_path, pos_x, pos_y, w, h):
        """
        Initializes the ImageButton object with the provided parameters.

        Args:
            window: Parent widget.
            image_path (str): Path to the image file.
            pos_x (int): The X-coordinate of the image position.
            pos_y (int): The Y-coordinate of the image position.
            w (int): The width of the image.
            h (int): The height of the image.
        """
        super().__init__(window)
        scale = QSize(w, h)
        pixmap = QPixmap(image_path)
        self.setPixmap(pixmap.scaled(scale))
        self.setStyleSheet("background-color: transparent;")
        self.resize(w, h)
        self.move(pos_x, pos_y)
        self.setCursor(QCursor(Qt.PointingHandCursor))

    def mousePressEvent(self, event):
        """
        Function to override the mouse press event to emit the clicked signal upon image button click.

        Args:
            event: Mouse press event.
        """
        # Emit a signal to indicate that the image was clicked
        self.clicked.emit()