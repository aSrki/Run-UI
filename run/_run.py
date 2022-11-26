import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import subprocess
import test

class Payload():
    def __init__(self):
        self.sto = None
        self.boja = None
        self.strategija = None
    def printPayload(self):
        print('Sto = ', self.sto)
        print('Boja = ', self.boja)
        print('Strategija = ', self.strategija)
        print('======================')

gamePayload = Payload()

class Screen1(QDialog):
    def __init__(self):
        super(Screen1, self).__init__()
        loadUi("/home/srdjan/Desktop/run/screen1.ui", self)
        
        self.button_sto1.clicked.connect(self.on_click_sto1)
        self.button_sto2.clicked.connect(self.on_click_sto2)
    
    def on_click_sto1(self):
        gamePayload.sto = 1
        #gamePayload.printPayload()
        self.gotoScreen2()
    
    def on_click_sto2(self):
        gamePayload.sto = 2
        #gamePayload.printPayload()
        self.gotoScreen2()

    def gotoScreen2(self):
        screen2 = Screen2()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Screen2(QDialog):
    def __init__(self):
        super(Screen2, self).__init__()
        loadUi("/home/srdjan/Desktop/run/screen2.ui", self)

        self.button_zelena.clicked.connect(self.on_click_zelena)
        self.button_plava.clicked.connect(self.on_click_plava)
        self.button_back.clicked.connect(self.gotoScreen1)

    def on_click_zelena(self):
        gamePayload.boja = 'zeleno'
        #gamePayload.printPayload()
        self.gotoScreen3()
    
    def on_click_plava(self):
        gamePayload.boja = 'plava'
        #gamePayload.printPayload()
        self.gotoScreen3()

    def gotoScreen1(self):
        screen1 = Screen1()
        widget.addWidget(screen1)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoScreen3(self):
        screen3 = Screen3()
        widget.addWidget(screen3)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class Screen3(QDialog):
    def __init__(self):
        super(Screen3, self).__init__()
        loadUi("/home/srdjan/Desktop/run/screen3.ui", self)

        self.button_pasivna.clicked.connect(self.on_click_pasivna)
        self.button_agresivna.clicked.connect(self.on_click_agresivna)
        self.button_back_3.clicked.connect(self.gotoScreen2)
        self.button_glhf.clicked.connect(self.glhf)
        self.button_glhf.hide()

    def on_click_pasivna(self):
        gamePayload.strategija = 'pasivna'
        self.button_glhf.show()
        #gamePayload.printPayload()
    
    def on_click_agresivna(self):
        gamePayload.strategija = 'agresivna'
        self.button_glhf.show()
        #gamePayload.printPayload()

    def gotoScreen2(self):
        screen2 = Screen2()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def glhf(self):
        #gamePayload.printPayload()
        Test = test.run()
        Test.start(gamePayload)
        


if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = QtWidgets.QStackedWidget()

    screen1 = Screen1()

    widget.addWidget(screen1)
    widget.showMaximized()
    widget.show()

    sys.exit(app.exec_())

