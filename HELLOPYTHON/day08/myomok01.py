import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui
from PyQt5.Qt import QSize, QRect



form_class = uic.loadUiType("myomok01.ui")[0]      
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.arr2D = [
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0]
            ]
        
        self.pb2D = []
        for i in range(10):
            pb_line = []
            for j in range(10):
                tmp = QPushButton(self)
                tmp.setToolTip(str(i)+","+str(j))
                tmp.setIconSize(QSize(40,40))
                tmp.setGeometry(QRect(40*j,i*40,40,40))
                tmp.setIcon(QtGui.QIcon('0.png'))
                tmp.clicked.connect(self.btnClick)
                pb_line.append(tmp)
            self.pb2D.append(pb_line) 
        self.myrender()    
    
    def myrender(self):
        b=0
        w=0
        for i in range(10):
            for j in range(10):
                if self.arr2D[i][j] == 0 :   
                    self.pb2D[i][j].setIcon(QtGui.QIcon('0.png'))
                
                if self.arr2D[i][j] == 1 :                 
                    b += 1
                    w = 0
                    self.pb2D[i][j].setIcon(QtGui.QIcon('1.png'))   
                
                if self.arr2D[i][j] == 2 :
                    w += 1
                    b = 0                 
                    self.pb2D[i][j].setIcon(QtGui.QIcon('2.png'))
                    
                if w == 5:
                    print("흰색승리")
                if b == 5:
                    print("검정승리")   
                
                    
    def btnClick(self): 
        print(self.sender().toolTip())
        i = int(self.sender().toolTip().split(',')[0])
        j = int(self.sender().toolTip().split(',')[1])
        if self.arr2D[i][j]==0:
            self.arr2D[i][j]=1
        elif self.arr2D[i][j]==1:
            self.arr2D[i][j]=2
        self.myrender() 
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()
    
    