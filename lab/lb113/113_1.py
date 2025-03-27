from matplotlib import pyplot as plt
import numpy as np


W = [29.49955502, 26.36843434, 8.806931406, 26.95486497, 23.13259391]
T = [26.54, 24.16, 10.34, 27.3, 22.42]
A = 0.952072503

plt.minorticks_on()
plt.grid(visible=True, axis='both', which='major')
plt.grid(visible=True, axis='both', which='minor', alpha=0.2)

plt.xlabel('$\omega$, рад/с - частота вращения маховика')
plt.ylabel("T, с - период прецессии")
plt.title('''Зависимость периода прецессии от частоты вращения маховика''', fontsize=10)

dat = np.array([W, T]).T
dat = dat.tolist()
dat = sorted(dat)
dat = np.array(dat)
print(dat)

plt.plot(dat.T[0], dat.T[1], marker='.', color='black', markersize=10)
plt.plot([7, 30], [7*A, A*30], color='pink', markersize=10)
plt.legend(['эксперементальная зависимость', 'аппроксимация'])

plt.show()