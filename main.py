import sys
from events import Events
from gui import EvningWindow, MorningWindow
from PyQt5.QtWidgets import QApplication
import datetime
from city_weather import get_weather

if __name__ == '__main__':
    app = QApplication(sys.argv)
    hour = datetime.datetime.now().hour.real
    cur_wather = get_weather()
    if 3 < hour < 15:
        events = Events(suffix='_morning', other_data=cur_wather)
        gui = MorningWindow(events)
    else:
        events = Events(suffix='_evening', other_data=cur_wather)
        gui = EvningWindow(events)
    sys.exit(app.exec_())
