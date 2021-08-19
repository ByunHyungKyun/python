import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.Qt import QSize, QRect
from sqlalchemy.sql.expression import except_

form_class = uic.loadUiType("myomok01.ui")[0]      
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.flag_wb=True
        self.flag_ing=True
        self.pb.clicked.connect(self.btnClick2)
        self.arr2D = [
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0],
                
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0],

                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0],
                
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0]
            ]
        
        self.pb2D = []
        for i in range(19):
            pb_line = []
            for j in range(19):
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
        for i in range(19):
            for j in range(19):
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
                      
                      
    def btnClick2(self):
        self.flag_wb = True
        self.flag_ing = True
        
        for i in range(19):
            for j in range(19): 
                self.arr2D[i][j]=0   
        self.myrender() 
        
                             
    def btnClick(self): 
        if self.flag_ing:
            print(self.sender().toolTip())
            i = int(self.sender().toolTip().split(',')[0])
            j = int(self.sender().toolTip().split(',')[1])
            
            if self.arr2D[i][j]>0:
                return
            stone = 0
            if self.flag_wb:
                self.arr2D[i][j]=1
                stone = 1
            else :
                self.arr2D[i][j]=2
                stone = 2
    
            up = self.getUP(i,j,stone)
            dw = self.getDW(i,j,stone)
            le = self.getLE(i,j,stone)
            ri = self.getRI(i,j,stone)
            dl = self.getDL(i,j,stone)
            ur = self.getUR(i,j,stone)
            dr = self.getDR(i,j,stone)
            ul = self.getUL(i,j,stone)
        
            D1 = up+dw+1
            D2 = le+ri+1
            D3 = dl+ur+1
            D4 = dr+ul+1
            self.myrender() 
    
            if D1==5 or D2==5 or D3==5 or D4==5:
                if self.flag_wb:
                    QtWidgets.QMessageBox.about(self, "오목", "흑돌 승리")
                    self.flag_ing = not self.flag_ing
                else :
                    QtWidgets.QMessageBox.about(self, "오목", "백돌 승리")
                    self.flag_ing = not self.flag_ing
            self.flag_wb = not self.flag_wb
        else:
            return
        
    def getUP(self,i,j,stone):
        cnt=0
        try:
            while True:
                i += -1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1    
                else :
                    return cnt
        except : 
            return cnt
        
    def getDW(self,i,j,stone):
        cnt=0
        try:
            while True:
                i += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1    
                else :
                    return cnt
        except : 
            return cnt
        
    def getLE(self,i,j,stone):
        cnt=0
        try:
            while True:
                j += -1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1    
                else :
                    return cnt
        except : 
            return cnt    
        
    def getRI(self,i,j,stone):
        cnt=0
        try:
            while True:
                j += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1    
                else :
                    return cnt
        except : 
            return cnt    
        
        
    def getDL(self,i,j,stone):
        cnt=0
        try:
            while True:
                i += 1
                j += -1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1    
                else :
                    return cnt
        except : 
            return cnt    
        
    def getUR(self,i,j,stone):
        cnt=0
        try:
            while True:
                i += -1
                j += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1    
                else :
                    return cnt
        except : 
            return cnt     
        
    def getUL(self,i,j,stone):
        cnt=0
        try:
            while True:
                i += -1
                j += -1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1    
                else :
                    return cnt
        except : 
            return cnt    

    def getDR(self,i,j,stone):
        cnt=0
        try:
            while True:
                i += 1
                j += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1    
                else :
                    return cnt
        except : 
            return cnt    
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()
    
    
    
    
    
    
    
    
    
    
    
    
    
    