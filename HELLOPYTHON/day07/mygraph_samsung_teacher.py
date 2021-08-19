from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import pymysql
from day07.myselect import getPrices

sam=getPrices("삼성전자")
lg=getPrices("LG전자")
h=getPrices("흥아해운")

fig = plt.figure()
ax = plt.axes(projection='3d')
z = np.array(sam)
x = np.array([1,1,1,1,1,1,1,1,1,1])
y =np.array([0,1,2,3,4,5,6,7,8,9])

z2 = np.array(lg)
x2 = np.array([1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5])
y2 =np.array([0,1,2,3,4,5,6,7,8,9])

z3 = np.array(h)
x3 = np.array([0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5])
y3 =np.array([0,1,2,3,4,5,6,7,8,9])

ax.plot3D(x, y, z, 'blue')
ax.plot3D(x2, y2, z2, 'red')
ax.plot3D(x3, y3, z3, 'maroon')
ax.set_title('3D line jusic')
plt.show()

















