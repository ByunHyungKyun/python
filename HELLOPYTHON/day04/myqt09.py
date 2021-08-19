import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import *
from PyQt5 import uic
from tkinter import messagebox
import random

form_class = uic.loadUiType("myqt09.ui")[0]      
class WindowClass(QMainWindow, form_class) :
    
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        self.pb1.clicked.connect(self.btnClick1)
        self.pb2.clicked.connect(self.btnClick2)
        self.pb3.clicked.connect(self.btnClick3)
        self.pb4.clicked.connect(self.btnClick4)
        self.pb5.clicked.connect(self.btnClick5)
        self.pb6.clicked.connect(self.btnClick6)
        self.pb7.clicked.connect(self.btnClick7)
        self.pb8.clicked.connect(self.btnClick8)
        self.pb9.clicked.connect(self.btnClick9)
        self.pb0.clicked.connect(self.btnClick0)
        self.pb.clicked.connect(self.btnClick)
        self.pbCall.clicked.connect(self.btnClickC)
        
        
        
    def btnClick(self): 
        a = self.pb.text()
        c = self.le.text()
        self.le.setText(c+a)
    def btnClick1(self): 
        a = self.pb1.text()
        c = self.le.text()
        self.le.setText(c+a)  
    def btnClick2(self): 
        a = self.pb2.text()
        c = self.le.text()
        self.le.setText(c+a)    
    def btnClick3(self): 
        a = self.pb3.text()
        c = self.le.text()
        self.le.setText(c+a)    
    def btnClick4(self): 
        a = self.pb4.text()
        c = self.le.text()
        self.le.setText(c+a)    
    def btnClick5(self): 
        a = self.pb5.text()
        c = self.le.text()
        self.le.setText(c+a)   
    def btnClick6(self): 
        a = self.pb6.text()
        c = self.le.text()
        self.le.setText(c+a)    
    def btnClick7(self): 
        a = self.pb7.text()
        c = self.le.text()
        self.le.setText(c+a)
    def btnClick8(self): 
        a = self.pb8.text()
        c = self.le.text()
        self.le.setText(c+a)
    def btnClick9(self): 
        a = self.pb9.text()
        c = self.le.text()
        self.le.setText(c+a)
    def btnClick0(self): 
        a = self.pb0.text()
        c = self.le.text()
        self.le.setText(c+a)
    def btnClickC(self): 
        c = self.le.text()
        messagebox.showinfo("Calling~", c)     
                       
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()