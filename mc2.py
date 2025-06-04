import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def InCircle(x, y, r):  # 円の内部ならTrue, 外部ならFalse
    return x * x + y * y < r * r

def ransu():  # -1 to 1 の一様乱数
    return 2 * np.random.rand() - 1

N = 1000
cn = 0
xin = []
yin = []
xout = []
yout = []

plt.ion()  # 対話モードON
fig = plt.figure()
ax = plt.axes()
# 円と正方形を描く
c = patches.Circle(xy=(0, 0), radius=1., ec='red', fill=False)
r = patches.Rectangle(xy=(-1, -1), width=2., height=2., ec='black', fill=False)
ax.add_patch(c)
ax.add_patch(r)
plt.axis('scaled')
ax.set_aspect('equal')

for n in range(1, N):
    x = ransu()
    y = ransu()
    if InCircle(x, y, 1):
        cn += 1
        xin.append(x)
        yin.append(y)
        ax.scatter(x, y, c='red', s=5)
    else:
        xout.append(x)
        yout.append(y)
        ax.scatter(x, y, c='black', s=5)
    fig.suptitle(f"Monte Carlo method  pi={4*cn/n:.5f}", fontsize=20)
    plt.pause(0.001)  # 少し待つことでアニメーション表示

plt.ioff()
plt.show()