from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QSlider, QVBoxLayout,
                             QPushButton, QGroupBox, QTextEdit,
                             QGridLayout, QLabel, QMessageBox)
import datetime


class BaseWindow(QWidget):
    def __init__(self, events):
        super().__init__()
        self.events = events
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 320)
        self.setWindowTitle('My sleep story')
        self.createGridLayout()
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
        self.show()

    def save(self):
        self.events(self.text_edit.toPlainText(), self.slide_feeling.value())

    def createGridLayout(self):
        date = datetime.datetime.now()
        self.horizontalGroupBox = QGroupBox("Good morning! Today is " + date.strftime("%d/%m/%Y"))

        self.btn_save = QPushButton('Save a data')
        self.btn_save.setToolTip('Push it if you want to save this day!')
        self.btn_save.clicked.connect(self.save)

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

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Quit',
                                     "Are you sure to quit?",
                                     QMessageBox.Yes,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
