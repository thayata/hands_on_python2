import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def InCircle(x,y,r):  #円の内部ならTrue, 外部ならFalse
    return  x*x + y*y < r*r 

def ransu():     # -1 to 1 の一様乱数
    return 2*np.random.rand()-1

N=1000
cn=0
xin=[]
yin=[]
xout=[]
yout=[]
for n in range(1,N):
    x=ransu()
    y=ransu()
    if InCircle(x,y,1): #円の内部か否か判断　Trueが内部
        cn += 1
        xin.append(x)
        yin.append(y)
    else:
        xout.append(x)
        yout.append(y)
    print("pi = ", 4*cn/n)

fig = plt.figure()
ax = plt.axes()
ax.scatter(xin,yin,c='red')  #点を打つ
ax.scatter(xout,yout,c='black')
#円を描く
c = patches.Circle(xy=(0, 0), radius=1.,  ec='red', fill=False)
#正方形を描く
r = patches.Rectangle(xy=(-1, -1), width=2., height=2., ec='black', fill=False)
ax.add_patch(c)
ax.add_patch(r)

fig.suptitle("Monte Carlo method  pi="+str(4*cn/n), fontsize = 20)
plt.axis('scaled')
ax.set_aspect('equal')
plt.show()
