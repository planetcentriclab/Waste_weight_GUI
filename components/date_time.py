
from PyQt5.QtCore import *

class DateTimeUpdater(QObject):
    """
    A class to continuously update date and time information and emit signals upon changes.

    Attributes:
        date_time_changed (pyqtSignal): Signal emitted upon updating date and time information.

    Methods:
        __init__: Initializes the DateTimeUpdater object and starts a QTimer for continuous updating.
        update_date_time: Updates date and time information and emits the date_time_changed signal.
    """

    date_time_changed = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_date_time)
        self.timer.start(1000)  # Update every second

    def update_date_time(self):
        """
        Function to update date and time information and emits the date_time_changed signal.
        """
        # Create a QLocale object for Thai locale
        thai_locale = QLocale(QLocale.Thai)
        current_datetime = QDateTime.currentDateTime()

        # Extract individual components
        datetime = current_datetime.date()  # Date
        day = datetime.dayOfWeek()  # Day of the week (1: Monday, 2: Tuesday, ..., 7: Sunday)
        month = datetime.month()  # Month (1: January, 2: February, ..., 12: December)
        year = datetime.year() + 543  # Year
        date = current_datetime.toString("dd")
        hour = '{:02d}'.format(current_datetime.time().hour())
        minute = '{:02d}'.format(current_datetime.time().minute())
        second = '{:02d}'.format(current_datetime.time().second())

        # Format the day, month, and year in Thai
        day_thai = thai_locale.dayName(day, QLocale.LongFormat)  # Long format (วันจันทร์, วันอังคาร, etc.)
        month_thai = thai_locale.monthName(month, QLocale.LongFormat)  # Long format (มกราคม, กุมภาพันธ์, etc.)

        current_datetime_text = f"{day_thai}ที่ {str(date)} เดือน{month_thai} พ.ศ.{year}, เวลา {str(hour)}:{str(minute)}:{str(second)} น."

        self.date_time_changed.emit(current_datetime_text)