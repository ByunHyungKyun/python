from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import pymysql
from day07.myselect2 import getPrices
from day07.myselect3 import getName
import random

fig = plt.figure()
ax = plt.axes(projection='3d')
arr = getName()
for i,item in enumerate(arr):
    color=["blue", "coral", "green", "purple", "yellow","black","pink"]
    if i<2:
        price = getPrices(item)
        z = np.array(price)
        x = np.array([i,i,i,i,i,i,i,i,i,i])
        y =np.array([0,1,2,3,4,5,6,7,8,9])
        ax.plot3D(x, y, z, color[random.randint(0,6)])
        ax.set_title('3D line jusic')
        print(str(i)+"완료")

plt.show()




