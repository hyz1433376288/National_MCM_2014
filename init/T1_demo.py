import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

W = 120
H = 50
R = H / 2
thick = 3
height = 53 - thick

slice_width = 2.5
N = 10

L = [0] * N
dL = [0] * N
leg = []
L[0] = 25
dL[0] = 25 * 2
# print("test:", math.sqrt(R ** 2 - (10 * 2.5) ** 2))
R = 25
for i in range(1, 10):
    # dL[i] = math.sqrt(R ** 2 - (i * 2.5) ** 2)
    # dL[i] = math.sqrt(125*i - 6.25*i**2)
    dL[10 - i] = math.sqrt(R ** 2 - (R - (i - 0.5) * 2.5) ** 2)
    print("i = ", 10 - i, "len = ", dL[10 - i])
    L[10 - i] = dL[10 - i]
    dL[10 - i] *= 2
    # L[i]  = L[i] * 100

# length of every leg
for i in L:
    leg.append(W / 2 - i)
print(len(dL))

# set matrix values to draw
mat = np.random.rand(50, 50)
for y in range(0, 50):
    for i in range(0, 5):
        for x in range(0, 50):
            if y / 5 >= 10:
                break
            if x <= dL[int(y / 5)]:
                mat[y, x] = 1
            else:
                mat[y, x] = 0
        y = y + 1
# draw
plt.matshow(mat, cmap=plt.cm.gray)
plt.show()

# caculate theta_i
theta = [0] * N
A = (W / 2) - L[-1]
B = height
C = math.sqrt(A ** 2 - B ** 2)
print("height:", height, "@#@", (W / 2 - L[-1]))

theta_i = N - 1
print(L)
while theta_i >= 0:
    c = (C / 2 - (L[theta_i] - L[-1]))
    if theta_i == N - 1:
        c = C / 2
    b = 25
    print("c = ", c, "b = ", b)
    theta[theta_i] = math.degrees(math.atan(c / b))
    theta_i -= 1
print(theta)

# calculate the length of slot
slot_end = []
slot_beg = []
slot_len = []
for i in range(N):
    slot_beg.append(leg[i] - leg[-1] / 2)
    slot_end.append((B / 2) / math.cos(math.radians(theta[i])))
    slot_len.append(slot_end[-1] - slot_beg[-1])

# calculate point of edge curve
X = []
Y = []
Z = []


for i in range(N):
    Z.append(- leg[i] * math.cos(math.radians(theta[i])))
    # Y.append(R * math.sqrt(R**2 - L[i]**2))
    Y.append(2.5 / 2 + 2.5 * i)
    X.append(L[i] + leg[i] * math.sin(math.radians(theta[i])))

dX = X[::-1]
dX += X

dY = [-y for y in Y]
dY.reverse()
dY += Y

dZ = Z[::-1]
dZ += Z
pd.DataFrame({
    'dX': dX,
    'dY': dY,
    'dZ': dZ
}).to_excel("point.xlsx", index=False)
print("write ovet")
# exit()

# write to excel
pd.DataFrame({
    'L': L,
    'leg': leg,
    'Degree': theta,
    'Slot_beg':slot_beg,
    'slot_end':slot_end,
    'slot_len':slot_len,
    "X":X,
    'Y':Y,
    'Z':Z
}).to_excel("result.xlsx")
print("-----------------------------write over!---------------------------------")
#
# import matplotlib as mpl
# from mpl_toolkits.mplot3d import Axes3D
# import numpy as np
# import matplotlib.pyplot as plt
#
# # 设置图例字号
# mpl.rcParams['legend.fontsize'] = 10
#
# # 方式2：设置三维图形模式
# fig = plt.figure()
# ax = fig.gca(projection='3d')
#
# # 测试数据
# theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
#
# # 绘制图形
# ax.plot(X, Y, Z, label='parametric curve')
#
# # 显示图例
# ax.legend()
#
# # 显示图形
# plt.show()
