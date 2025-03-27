from matplotlib import pyplot as plt
import matplotlib
import numpy as np

plt.minorticks_on()
plt.grid(visible=True, axis='both', which='major')
plt.grid(visible=True, axis='both', which='minor', alpha=0.2)

plt.xlabel('a, м/с² - ускорение тележки')
plt.ylabel("T, мH - сила натяжения нити")
plt.title('''Зависимость силы натяжения нити от ускорения тележки''', fontsize=10)

dots = [[0.061,	17.47],
[0.072,	25.64],
[0.172,	33.48],
[0.235,	41.41],
[0.320,	49.12],
[0.450,	56.40],
[0.536,	63.13]]
dots = np.array(dots).T
plt.scatter(dots[0], dots[1], marker='.', color="black")
plt.plot([0, 0.55], [17.43194543, 0.55*89.1230487 + 17.43194543], color="red")
plt.legend(['эксперементальные точки', 'аппроксимация'])

plt.show()