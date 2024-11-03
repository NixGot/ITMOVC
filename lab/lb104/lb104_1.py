from matplotlib import pyplot as plt
import matplotlib
import numpy as np


#y = 0,0139x + 0.0235
#y = 0,0125x + 0,0350
#y = 0,0197x + 0,0428	
#y = 0,0179x + 0,0606	
#y = 0,0175x + 0,0781
#y = 0,0190x + 0,0966




plt.ylim(0, 0.3)
plt.xlim(0, 10)
plt.minorticks_on()
plt.grid(visible=True, axis='both', which='major')
plt.grid(visible=True, axis='both', which='minor', alpha=0.2)

x1 = [1.913559593, 4.106565371, 6.095734379, 8.1077262]
x2 = [1.339924742, 2.732223374, 4.282698479, 5.45641339]
x3 = [0.941646946, 2.166947854, 3.115700191, 4.422342559]
x4 = [0.67303735, 1.514334037, 2.396288628, 3.073832355]
x5 = [0.543787054, 1.148517035, 1.893363854, 2.386807772]
x6 = [0.419204664, 0.941646946, 1.463122774, 1.947944522]
y1 = [0.059972933, 0.108823864, 0.157240587, 0.205183119]
y2 = [0.060053955, 0.109177926, 0.157918668, 0.206483278]
y3 = [0.060110209, 0.109323554, 0.158355129, 0.206990368]
y4 = [0.060148148, 0.109491683, 0.158624191, 0.207651655]
y5 = [0.060166404, 0.109585926, 0.158812286, 0.20798856]
y6 = [0.060184, 0.10963922, 0.158973198, 0.208203771]
a = np.array([0.013891645, 0.01249931, 0.019665211, 0.017895752, 0.01751762, 0.019045532])
b = np.array([0.023519762, 0.035017557, 0.042841547, 0.060637692, 0.078105415, 0.096568712])
c = [x1[0], x2[0], x3[0], x4[0], x5[0], x6[0]]
color = ['blue', 'orange', 'black', 'purple', 'green', 'red']
dots = np.stack((b, a, c), axis=1)

for i in range(len(dots)):
    plt.plot([0, dots[i][2]], [dots[i][1], dots[i][2]*dots[i][0] + dots[i][1]], linestyle='dashed', color=f'{color[i]}', linewidth=0.5)

c = [x1[3], x2[3], x3[3], x4[3], x5[3], x6[3]]
d = [x1[0], x2[0], x3[0], x4[0], x5[0], x6[0]]
dots = np.stack((b, a, c, d), axis=1)

for i in range(len(dots)):
    plt.plot([dots[i][2], dots[i][3]], [dots[i][2]*dots[i][0] + dots[i][1], dots[i][3]*dots[i][0] + dots[i][1]], color=f'{color[i]}', linewidth=0.5)

c = [9, 9, 9, 9, 9, 9]
d = [x1[3], x2[3], x3[3], x4[3], x5[3], x6[3]]
dots = np.stack((b, a, c, d), axis=1)

for i in range(len(dots)):
    plt.plot([0, dots[i][2]], [dots[i][1], dots[i][2]*dots[i][0] + dots[i][1]], linestyle='dashed', color=f'{color[i]}', linewidth=0.5)


plt.scatter(x1, y1, color='blue', s=8)
dat = np.stack((x1, y1), axis=1)
for i in dat:
    plt.plot([i[0]+0.052, i[0]-0.052], [i[1], i[1]])
    plt.plot([i[0], i[0]], [i[1]+0.0011, i[1]-0.0011])
plt.scatter(x2, y2, color='orange', s=8)
plt.scatter(x3, y3, color='black', s=8)
plt.scatter(x4, y4, color='purple', s=8)
plt.scatter(x5, y5, color='green', s=8)
plt.scatter(x6, y6, color='red', s=8)

plt.text(x1[3]+0.1, y1[3]-0.01, '1', color='blue')
plt.text(x1[3]-0.1, y1[3]-0.02, 'номер риски', color='blue', fontsize=6)
plt.text(x2[3]+0.1, y2[3]-0.01, '2', color='orange')
plt.text(x3[3]+0.1, y3[3]-0.01, '3', color='black')
plt.text(x4[3]+0.1, y4[3]-0.01, '4', color='purple')
plt.text(x5[3]+0.1, y5[3]-0.01, '5', color='green')
plt.text(x6[3]+0.1, y6[3]-0.01, '6', color='red')
plt.xlabel('ε, м/с² - угловое ускорение')
plt.ylabel("M, H·м - момент силы натяжения нити")
plt.title('''Эксперементальные точки зависимости момента силы натяжения нити от
           углового ускорения, и их линейные теоретические графики''', fontsize=10)




plt.show()