from operator import index
from PyQt5.QtWidgets import QMainWindow, QApplication, QComboBox, QLabel
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        ##load ui file
        uic.loadUi("Window.ui", self)

        #define our widgets
        self.combo1 = self.findChild(QComboBox ,"comboBox")
        self.combo2 = self.findChild(QComboBox ,"comboBox_2")
        self.label = self.findChild(QLabel ,"label")

        #Add items to combobox
        self.combo1.addItem("male",["john", "wes", "Dan"])
        self.combo1.addItem("female", ["April", "steph", "Beth"])
        
        #Click the 1st opert
        self.combo1.activated.connect(self.clicker)

        ##show app
        self.show()

    def clicker(self, index):
            #clear second box
            self.combo2.clear()
            #Do the dependence
            self.combo2.addItems(self.combo1.itemData(index))
    
    def clicker2(self):
        self.label.setText(f'you picked: {self.combo2.currentText()} - {self.combo1.currentText()}')

##initialise app
app = QApplication(sys.argv)
UIWiWindow = UI()
app.exec_()        