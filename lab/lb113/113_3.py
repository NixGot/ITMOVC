from matplotlib import pyplot as plt
import numpy as np


W = [20.54601595, 18.71342024, 17.55103096, 14.82831732, 32.88200311]
T = [9.46, 9.47, 8.57, 8.34, 14.27]
A = 0.4681503

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
plt.plot([15, 33], [15*A, A*33], color='pink', markersize=10)
plt.legend(['эксперементальная зависимость', 'аппроксимация'])

plt.show()