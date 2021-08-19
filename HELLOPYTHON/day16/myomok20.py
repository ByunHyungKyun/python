import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.Qt import QSize, QRect
from sqlalchemy.sql.expression import except_
from tensorflow.keras.models import load_model
import numpy as np


model = load_model('models/20201213_202430.h5')


def getComIJ(arr2D):
    input = np.zeros((20,20))
    
    for i in range(20): 
        for j in range(20): 
            if arr2D[i][j] == 1:
                input[i][j]=1
            if arr2D[i][j] == 2 :
                input[i][j]=-1
    
    
    input = input.reshape((1,20,20,1))
    
    output = model.predict(input).squeeze()
    output = output.reshape((20, 20))
    
    for i in range(20):
        for j in range(20):
            if arr2D[i][j] > 0:
                output[i][j] = 0
    
    
    i,j= np.unravel_index(np.argmax(output), output.shape)
    return i,j


form_class = uic.loadUiType("myomok20.ui")[0]      
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.flag_wb=True
        self.flag_ing=True
        self.pb.clicked.connect(self.btnClick2)
        self.arr2D = [
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0,0],
                
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0,0],

                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0,0],
                
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0,0]
            ]
        
        self.arr_seq = [
                {'i':0,'j':0},
                {'i':0,'j':1},
                {'i':0,'j':2},
                {'i':0,'j':3},
                {'i':0,'j':4}
            ]
        
        self.arr_idx=0
        
        
        self.pb2D = []
        for i in range(20):
            pb_line = []
            for j in range(20):
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
        for i in range(20):
            for j in range(20):
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
        self.arr_idx = 0
        
        for i in range(20):
            for j in range(20): 
                self.arr2D[i][j]=0   
        self.myrender() 
        
                             
    def btnClick(self): 
        if not self.flag_ing:
            return
        
        
        str_ij=self.sender().toolTip()
        i = int(str_ij.split(',')[0])
        j = int(str_ij.split(',')[1])
            
        if self.arr2D[i][j]>0:
            return
       
       
       
        stone = 1
        self.arr2D[i][j]=1
    
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
            QtWidgets.QMessageBox.about(self, "오목", "흑돌 승리")
            self.flag_ing = not self.flag_ing
            return
        self.flag_wb = not self.flag_wb
    
        
        com_i,com_j=getComIJ(self.arr2D)
        print(com_i,com_j)
        
        stone = 2
        self.arr2D[com_i][com_j]=2
        self.arr_idx+=1
        
    
        up = self.getUP(com_i,com_j,stone)
        dw = self.getDW(com_i,com_j,stone)
        le = self.getLE(com_i,com_j,stone)
        ri = self.getRI(com_i,com_j,stone)
        dl = self.getDL(com_i,com_j,stone)
        ur = self.getUR(com_i,com_j,stone)
        dr = self.getDR(com_i,com_j,stone)
        ul = self.getUL(com_i,com_j,stone)
    
        D1 = up+dw+1
        D2 = le+ri+1
        D3 = dl+ur+1
        D4 = dr+ul+1
        self.myrender() 
    
        if D1==5 or D2==5 or D3==5 or D4==5:
            QtWidgets.QMessageBox.about(self, "오목", "백돌 승리")
            self.flag_ing = not self.flag_ing
        self.flag_wb = not self.flag_wb
        
        
        
        
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    