from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QSlider, QVBoxLayout,
                             QPushButton, QGroupBox, QTextEdit,
                             QGridLayout, QLabel, QMessageBox)
import datetime
import abc


class BaseWindow(QWidget):
    __metaclass__ = abc.ABCMeta

    def __init__(self, events, h, w):
        super().__init__()
        self.events = events
        self.setWindowTitle('My sleep story')
        self.setGeometry(300, 300, h, w)
        self._initUI()

    def _initUI(self):
        self._create_grid_layout()
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
        self.show()

    def _save(self):
        self.events(self.text_edit.toPlainText(), self.slide_feeling.value())

    @abc.abstractmethod
    def _create_grid_layout(self):
        pass

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Quit',
                                     "Are you sure to quit?",
                                     QMessageBox.Yes,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class MorningWindow(BaseWindow):
    def __init__(self, events):
        super().__init__(events, 500, 100)

    def _create_grid_layout(self):
        date = datetime.datetime.now()
        self.horizontalGroupBox = QGroupBox("Good morning! Today is " + date.strftime("%d/%m/%Y"))

        self.btn_save = QPushButton('Save a data')
        self.btn_save.setToolTip('Push it if you want to save this day!')
        self.btn_save.clicked.connect(self._save)

        self.slide_feeling = QSlider(Qt.Horizontal)
        self.slide_feeling.setMinimum(0)
        self.slide_feeling.setMaximum(10)
        self.slide_feeling.setSliderPosition(5)
        self.slide_feeling.setToolTip('The left is the worst and the right is the best.')

        grid = QGridLayout()
        grid.setSpacing(6)
        grid.addWidget(QLabel('How do you feel?'), 2, 0)
        grid.addWidget(self.slide_feeling, 3, 0)
        grid.addWidget(self.btn_save, 5, 0)

        self.horizontalGroupBox.setLayout(grid)


class EvningWindow(BaseWindow):
    def __init__(self, events):
        super().__init__(events, 500, 300)

    def _create_grid_layout(self):
        date = datetime.datetime.now()
        self.horizontalGroupBox = QGroupBox("Good night! Today is " + date.strftime("%d/%m/%Y"))

        self.btn_save = QPushButton('Save a data')
        self.btn_save.setToolTip('Push it if you want to save this day!')
        self.btn_save.clicked.connect(self._save)

        self.text_edit = QTextEdit()

        self.slide_feeling = QSlider(Qt.Horizontal)
        self.slide_feeling.setMinimum(0)
        self.slide_feeling.setMaximum(10)
        self.slide_feeling.setSliderPosition(5)
        self.slide_feeling.setToolTip('The left is the worst and the right is the best.')

        grid = QGridLayout()
        grid.setSpacing(6)
        grid.addWidget(QLabel('Describe your state of health'), 0, 0)
        grid.addWidget(self.text_edit, 1, 0, 1, 1)
        grid.addWidget(QLabel('How do you feel?'), 2, 0)
        grid.addWidget(self.slide_feeling, 3, 0)
        grid.addWidget(self.btn_save, 5, 0)

        self.horizontalGroupBox.setLayout(grid)
