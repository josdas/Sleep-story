import sys
from events import Events
from gui import EvningWindow, MorningWindow
from PyQt5.QtWidgets import QApplication
import datetime

if __name__ == '__main__':
    app = QApplication(sys.argv)
    hour = datetime.datetime.now().hour.real
    if hour > 3 and hour < 15:
        events = Events(suffix='morning')
        gui = MorningWindow(events)
    else:
        events = Events(suffix='evning')
        gui = EvningWindow(events)
    sys.exit(app.exec_())
