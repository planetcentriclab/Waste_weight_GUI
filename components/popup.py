from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from components.shape import *
from components.color import *

class PopupDialog(QDialog):
    """
    A class representing a simple popup dialog with a text label and an "OK" button.

    Attributes:
        color_overlay (QColor): Color for overlaying the background.
        line_color_pop_up (QColor): Color for the border of the popup dialog.
        bg_color_pop_up (QColor): Background color of the popup dialog.
        pos_x (int): X-coordinate position of the popup dialog.
        pos_y (int): Y-coordinate position of the popup dialog.
        w (int): Width of the popup dialog.
        h (int): Height of the popup dialog.
        x_radius (int): X-axis radius for rounding the corners of the popup dialog.
        y_radius (int): Y-axis radius for rounding the corners of the popup dialog.

    Methods:
        __init__: Initializes the PopupDialog object with provided parameters.
        paintEvent: Paints the overlay and the background of the popup dialog.
    """
    def __init__(self, color_overlay, line_color_pop_up, bg_color_pop_up, pos_x, pos_y, w, h, x_radius, y_radius, text, width_text, size_y, text_font_name, text_font_size, width_button, height_button, style_button, parent=None):
        super().__init__(parent, Qt.FramelessWindowHint)  # No title bar
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.color_overlay = color_overlay
        self.line_color_pop_up = line_color_pop_up
        self.bg_color_pop_up = bg_color_pop_up
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.w = w
        self.h = h
        self.x_radius = x_radius
        self.y_radius = y_radius

        desktop = QApplication.desktop()
        screen_rect = desktop.screenGeometry()

        self.resize(screen_rect.width(), screen_rect.height())
        # Create a layout for the button
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout) 

        # Create a label for the text
        self.text_label = QLabel(text)
        self.text_label.setFixedWidth(width_text)
        self.text_label.setFixedHeight(size_y)
        self.text_label.setFont(QFont(text_font_name, text_font_size))
        self.text_label.setAlignment(Qt.AlignCenter)
        self.text_label.setStyleSheet(f"color: {Color.darkgreen}; background-color: transparent; font-weight: bold;")
        layout.addWidget(self.text_label, alignment=Qt.AlignCenter)

        # Create a OK button
        self.button = QPushButton("ตกลง", clicked=self.close)
        self.button.setFont(QFont(text_font_name, text_font_size))
        self.button.setMinimumSize(width_button, height_button)
        self.button.setMaximumSize(width_button, height_button) 
        self.button.setStyleSheet(style_button)
        self.button.setCursor(QCursor(Qt.PointingHandCursor))
        layout.addWidget(self.button, alignment=Qt.AlignCenter)
    
    def paintEvent(self, event):
        """
        Function to paint the overlay and the background of the popup dialog.

        Args:
            event: Paint event.
        """
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setPen(self.color_overlay)
        painter.setBrush(self.color_overlay)
        painter.drawRect(0, 0, self.size().width(), self.size().height())

        self.pop_up_background = Rectangle(painter, self.line_color_pop_up, self.bg_color_pop_up, self.pos_x, self.pos_y, self.w, self.h, self.x_radius, self.y_radius)

class PopupDialogSetting(QDialog):
    """
    A class representing a customizable popup dialog for settings.
    This dialog contains a text label, an input text field, a "Cancel" button, and a "Save" button.

    Methods:
        __init__: Initializes the PopupDialogSetting object with provided parameters.
        paintEvent: Paints the overlay and the background of the popup dialog.
        get_input: Returns the text entered in the input text field.
        show_error_message: Displays an error message in the input text field.
        keyPressEvent: Handles key press events, preventing dialog closure on Enter key press.
    """

    def __init__(self, color_overlay, line_color_pop_up, bg_color_pop_up, pos_x, pos_y, w, h, x_radius, y_radius, text, width_text, size_y, text_font_name, text_font_size, width_button, height_button, style_button, style_input_text, placeholder_init, Goto, parent=None):
        """
        Initializes the PopupDialogSetting object with provided parameters.

        Args:
            color_overlay (QColor): Color for overlaying the background.
            line_color_pop_up (QColor): Color for the border of the popup dialog.
            bg_color_pop_up (QColor): Background color of the popup dialog.
            pos_x (int): X-coordinate position of the popup dialog.
            pos_y (int): Y-coordinate position of the popup dialog.
            w (int): Width of the popup dialog.
            h (int): Height of the popup dialog.
            x_radius (int): X-axis radius for rounding the corners of the popup dialog.
            y_radius (int): Y-axis radius for rounding the corners of the popup dialog.
            text (str): Text to be displayed in the dialog.
            width_text (int): Width of the text label.
            size_y (int): Height of the text label.
            text_font_name (str): Name of the font for the text label.
            text_font_size (int): Font size for the text label.
            width_button (int): Width of the buttons.
            height_button (int): Height of the buttons.
            style_button (str): Style sheet for the buttons.
            style_input_text (str): Style sheet for the input text field.
            placeholder_init (str): Placeholder text for the input text field.
            Goto: Function to execute upon clicking the "Save" button.
            parent: Parent widget (default is None).
        """
        super().__init__(parent, Qt.FramelessWindowHint)  # No title bar
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.color_overlay = color_overlay
        self.line_color_pop_up = line_color_pop_up
        self.bg_color_pop_up = bg_color_pop_up
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.w = w
        self.h = h
        self.x_radius = x_radius
        self.y_radius = y_radius

        desktop = QApplication.desktop()
        screen_rect = desktop.screenGeometry()

        self.resize(screen_rect.width(), screen_rect.height()-15)
        # Create a layout for the button
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(15, 0, 0, 0)
        self.setLayout(layout) 

        layout1 = QHBoxLayout()
        layout1.setSpacing(50)

        self.text_label_blank = QLabel()
        self.text_label_blank.setFixedWidth(50)
        self.text_label_blank.setFixedHeight(50)
        layout.addWidget(self.text_label_blank, alignment=Qt.AlignCenter)

        # Create a label for the text
        self.text_label = QLabel(text)
        self.text_label.setFixedWidth(width_text)
        self.text_label.setFixedHeight(size_y)
        self.text_label.setFont(QFont(text_font_name, text_font_size))
        self.text_label.setAlignment(Qt.AlignCenter)
        self.text_label.setStyleSheet(f"color: {Color.darkgreen}; background-color: transparent; font-weight: bold;")
        layout.addWidget(self.text_label, alignment=Qt.AlignCenter)

        # Create input text
        self.input_text = QLineEdit()
        self.input_text.setFont(QFont(text_font_name, text_font_size))
        self.input_text.setCursor(QCursor(Qt.IBeamCursor))
        self.input_text.setPlaceholderText(placeholder_init)
        self.input_text.setStyleSheet(style_input_text)
        self.input_text.setMinimumSize(width_button + 300, height_button)
        self.input_text.setMaximumSize(width_button + 300, height_button) 
        layout.addWidget(self.input_text, alignment=Qt.AlignCenter)

        self.text_label_blank = QLabel()
        self.text_label_blank.setFixedWidth(10)
        self.text_label_blank.setFixedHeight(10)
        layout.addWidget(self.text_label_blank, alignment=Qt.AlignCenter)

        # Create a cancel button
        self.button_cancel= QPushButton("ยกเลิก")
        self.button_cancel.clicked.connect(self.close)
        self.button_cancel.setFont(QFont(text_font_name, text_font_size))
        self.button_cancel.setMinimumSize(width_button, height_button)
        self.button_cancel.setMaximumSize(width_button, height_button) 
        self.button_cancel.setStyleSheet(style_button)
        self.button_cancel.setCursor(QCursor(Qt.PointingHandCursor))
        layout1.addWidget(self.button_cancel, alignment=Qt.AlignRight)

        # Create a save button
        self.button_save = QPushButton("บันทึก")
        self.button_save.clicked.connect(Goto)
        self.button_save.setFont(QFont(text_font_name, text_font_size))
        self.button_save.setMinimumSize(width_button, height_button)
        self.button_save.setMaximumSize(width_button, height_button) 
        self.button_save.setStyleSheet(style_button)
        self.button_save.setCursor(QCursor(Qt.PointingHandCursor))
        layout1.addWidget(self.button_save, alignment=Qt.AlignLeft)
        
        layout.addLayout(layout1)
    
    def paintEvent(self, event):
        """
        Function to paint the overlay and the background of the popup dialog.

        Args:
            event: Paint event.
        """
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setPen(self.color_overlay)
        painter.setBrush(self.color_overlay)
        painter.drawRect(0, 0, self.size().width(), self.size().height())
        self.pop_up_background = Rectangle(painter, self.line_color_pop_up, self.bg_color_pop_up, self.pos_x, self.pos_y, self.w, self.h, self.x_radius, self.y_radius)

    def get_input(self):
        """
        Function to return the text entered in the input text field.

        Returns:
            str: Text entered in the input text field.
        """
        return self.input_text.text()
    
    def show_error_message(self):
        """
        Function to clear the input text field and displays an error placeholder text.
        """
        self.input_text.clear()
        self.input_text.setPlaceholderText("ไม่มีชื่อในระบบ กรุณาใส่ชื่อใหม่อีกครั้ง")

    def keyPressEvent(self, event):
        """
        Function to prevents closing the dialog when the Enter key is pressed.

        Args:
            event (QKeyEvent): The key press event.
        """
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            # Prevent closing the dialog on Enter key press
            event.ignore()