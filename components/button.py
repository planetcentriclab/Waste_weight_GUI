from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from components.color import *

class Button():
   """
   A class representing a button widget with customizable style and functionality.

   Attributes:
      window (QWidget): The parent window or widget.
      text (str): The text displayed on the button.
      font_name (str): The font family name.
      font_size (int): The font size.
      pos_x (int): The x-coordinate position of the button.
      pos_y (int): The y-coordinate position of the button.
      size_x (int): The width of the button.
      size_y (int): The height of the button.
      style (str): The style sheet for the button.
      Goto (function, optional): The function to call when the button is clicked.
      cursor (QCursor, optional): The cursor shape for the button.

   Methods:
      __init__: Initializes the Button object.
      Icon: Sets the icon for the button.
      disable: Disables the button.
      enable: Enables the button.
   """
   def __init__(self, window, text, font_name, font_size, pos_x, pos_y, size_x, size_y, style, Goto=None, cursor=None):
      self.style = style
      self.object = QPushButton(window)
      self.object.setText(text)
      self.object.setFont(QFont(font_name, font_size))
      self.object.resize(size_x, size_y)
      self.object.move(pos_x, pos_y)
      self.object.setStyleSheet(style)
      if Goto:
         self.object.clicked.connect(Goto)
      self.object.setCursor(QCursor(cursor))
      self.pressed = False
      self.ready = False

   def Icon(self, pic):
      """
      Function to set the icon for the button.

      Args:
         pic (QPixmap or QIcon): The icon to set for the button.
      """
      self.object.setIcon(pic)

   def disable(self, style=None):
      """
      Function to disable the button.

      Args:
         style (str, optional): The style sheet for the disabled button.
      """
      if style:
         self.object.setStyleSheet(style)
      self.object.setEnabled(False)

   def enable(self):
      """
      Function to enable the button.
      """
      self.object.setStyleSheet(self.style)
      self.object.setEnabled(True)

class ProfileButton(QGraphicsObject):
   """
   A class representing a profile button widget with customizable style and functionality.

   Attributes:
      clicked_text (pyqtSignal): A signal emitted when the button is clicked, carrying text and object data.
      window (QWidget): The parent window or widget.
      text (str): The text displayed on the button.
      font_name (str): The font family name.
      font_size (int): The font size.
      pos_x (int): The x-coordinate position of the button.
      pos_y (int): The y-coordinate position of the button.
      size_x (int): The width of the button.
      size_y (int): The height of the button.
      style (str): The style sheet for the button.
      blur_radius (int): The blur radius for the button's shadow effect.
      blur_color (QColor): The color of the button's shadow effect.
      width_text (int): The width of the text label.
      width_icon (int): The width of the icon label.
      Goto (function, optional): The function to call when the button is clicked.
      cursor (QCursor, optional): The cursor shape for the button.

   Methods:
      __init__: Initializes the ProfileButton object.
      set_icon: Sets the icon for the button.
      set_style: Sets the style for the button.
      enterEvent: Event handler for mouse enter event.
      leaveEvent: Event handler for mouse leave event.
      on_clicked: Event handler for button clicked event.
      text: Gets the text displayed on the button.
      disable: Disables the button.
      enable: Enables the button.
   """
   clicked_text = pyqtSignal(str, object)
   def __init__(self, window, text, font_name, font_size, pos_x, pos_y, size_x, size_y, style, blur_radius, blur_color, width_text, width_icon, Goto=None, cursor=None):
      super().__init__() 
      self.style = style
      self.blur_radius = blur_radius
      self.blur_color = blur_color
      self.text_font_name = font_name
      self.text_font_size = font_size
      self.object = QPushButton(window)
      self.object.resize(size_x, size_y)
      self.object.move(pos_x, pos_y)
      self.object.setStyleSheet(style)
      self.object.setCursor(QCursor(cursor))

      # Create a layout for the button
      layout = QHBoxLayout()
      layout.setAlignment(Qt.AlignCenter)
      layout.setContentsMargins(0, 0, 0, 0)
      self.object.setLayout(layout) 

      # Create a label for the icon
      self.icon_label = QLabel()
      self.icon_label.setFixedWidth(width_icon)
      self.icon_label.setFixedHeight(size_y)
      layout.addWidget(self.icon_label, alignment=Qt.AlignCenter)

      # Create a label for the text
      self.text_label = QLabel(text)
      self.text_label.setFixedWidth(width_text)
      self.text_label.setFixedHeight(size_y)
      self.text_label.setFont(QFont(self.text_font_name, self.text_font_size))
      self.text_label.setAlignment(Qt.AlignCenter)
      self.text_label.setStyleSheet(f"color: {Color.darkgreen}; background-color: transparent; font-weight: bold;")
      layout.addWidget(self.text_label, alignment=Qt.AlignCenter)
      layout.setSizeConstraint(QHBoxLayout.SetMinimumSize)

      # creating a QGraphicsDropShadowEffect object 
      shadow = QGraphicsDropShadowEffect() 
      shadow.setBlurRadius(blur_radius) 
      shadow.setColor(blur_color) 
      self.object.setGraphicsEffect(shadow) 

      self.object.enterEvent = self.enterEvent
      self.object.leaveEvent = self.leaveEvent

      # Connect clicked signal to slot
      self.object.clicked.connect(self.on_clicked)
      self.click_flag = False

   def set_icon(self, icon_path, icon_width, icon_height):
      """
      Function to set the icon for the button.

      Args:
         icon_path (str): The file path of the icon.
         icon_width (int): The width of the icon.
         icon_height (int): The height of the icon.
      """
      icon = QIcon(icon_path)
      self.icon_label.setAlignment(Qt.AlignCenter)
      self.icon_label.setPixmap(icon.pixmap(QSize(icon_width, icon_height)))
      self.icon_label.setStyleSheet("background-color: transparent;")
   
   def set_style(self, style, old_object=False):
      """
      Function to set the style for the button.

      Args:
         style (str): The style sheet for the button.
         old_object (bool, optional): Indicates if the previous style should be reset.
      """
      self.object.setStyleSheet(style)
      if old_object:
         self.click_flag = False
         self.text_label.setStyleSheet(f"color: {Color.darkgreen}; background-color: transparent; font-weight: bold;")
      
   def enterEvent(self, event):
      """
      Function to event handler for mouse enter event.
      """
      if not self.click_flag:
            self.text_label.setStyleSheet(f"color: {Color.white}; background-color: transparent; font-weight: bold;")

   def leaveEvent(self, event):
      """
      Function to event handler for mouse leave event.
      """
      if not self.click_flag:
         self.text_label.setStyleSheet(f"color: {Color.darkgreen}; background-color: transparent; font-weight: bold;")

   def on_clicked(self):
      """
      Function to event handler for button clicked event.
      """
      text = self.text_label.text()
      self.click_flag = True
      self.clicked_text.emit(text, self) 
   
   def text(self):
      """
      Function to return the text displayed on the button.

      Returns:
         str: Text entered in the input text field.
      """
      return self.text_label.text()

   def disable(self, style_disable=None):
      """
      Function to disable the button.

      Args:
         style (str, optional): The style sheet for the disabled button.
      """
      self.click_flag = True
      self.object.setEnabled(False)
      if style_disable:
         self.object.setStyleSheet(style_disable)
         self.text_label.setStyleSheet(f"color: {Color.darkgray}; background-color: transparent; font-weight: bold;")
         
         # creating a QGraphicsDropShadowEffect object 
         shadow = QGraphicsDropShadowEffect() 
         shadow.setBlurRadius(self.blur_radius) 
         shadow.setColor(QColor(255, 255, 255)) 
         self.object.setGraphicsEffect(shadow) 

   def enable(self):
      """
      Function to enable the button.
      """     
      self.click_flag = False
      self.object.setEnabled(True)
      self.object.setStyleSheet(self.style)
      self.text_label.setStyleSheet(f"color: {Color.darkgreen}; background-color: transparent; font-weight: bold;")
      
      # creating a QGraphicsDropShadowEffect object 
      shadow = QGraphicsDropShadowEffect() 
      shadow.setBlurRadius(self.blur_radius) 
      shadow.setColor(self.blur_color) 
      self.object.setGraphicsEffect(shadow) 