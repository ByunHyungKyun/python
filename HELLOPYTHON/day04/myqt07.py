import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random

form_class = uic.loadUiType("myqt07.ui")[0]      

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.btnClick)
    
    def btnClick(self): 
        a = self.le1.text();
        com = ""
        result = ""
        rand = random.random()
        
        if rand > 0.666:
            com = "가위"
        elif rand<0.666 and rand >0.333 :
            com = "바위"
        else :
            com = "보"
        
        if com == "가위":
            if a=="보":
                result = "짐"
            elif a=="바위":
                result = "이김"
            else :
                result = "비김"       
        elif com == "바위":
            if a=="보":
                result = "이김"
            elif a=="가위":
                result = "짐"
            else :
                result = "비김"
        else :
            if a=="가위":
                result = "이김"
            elif a=="바위":
                result = "짐"
            else :
                result = "비김"
        self.le2.setText(com)
        self.le3.setText(result)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()