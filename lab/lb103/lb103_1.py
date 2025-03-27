from matplotlib import pyplot as plt
import matplotlib
import numpy as np

plt.minorticks_on()
plt.grid(visible=True, axis='both', which='major')
plt.grid(visible=True, axis='both', which='minor', alpha=0.2)

plt.xlabel('a, м/с² - ускорение тележки')
plt.ylabel("T, мH - сила натяжения нити")
plt.title('''Зависимость силы натяжения нити от ускорения тележки''', fontsize=10)

dots = [[0.265,17.10],
[0.398,24.78],
[0.528,32.24],
[0.645,39.64],
[0.780,46.74],
[0.900,53.70],
[1.028,59.79]]
dots = np.array(dots).T
plt.scatter(dots[0], dots[1], marker='.', color="black")
plt.plot([0, 1.035], [2.451686701, 1.035*56.53441726 + 2.451686701], color="red")
plt.legend(['эксперементальные точки', 'аппроксимация'])

plt.show()