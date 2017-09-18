import sys
from events import Events
from gui import BaseWindow
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    events = Events()
    gui = BaseWindow(events)
    sys.exit(app.exec_())
