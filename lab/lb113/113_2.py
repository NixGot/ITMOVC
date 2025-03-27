from matplotlib import pyplot as plt
import numpy as np


W = [38.85102915, 29.52049897, 31.47875839, 28.89218044, 26.11710693]
T = [25.15, 20.81, 17.94, 16.72, 15.59]
A = 0.623158872

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
plt.plot([25, 40], [25*A, A*40], color='pink', markersize=10)
plt.legend(['эксперементальная зависимость', 'аппроксимация'])

plt.show()