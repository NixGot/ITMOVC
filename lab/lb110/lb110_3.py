from matplotlib import pyplot as plt
import numpy as np


w = [3.01, 3.07, 3.12, 3.18, 3.23, 3.28, 3.34, 3.39, 3.44, 3.50, 3.55, 3.60, 3.66, 3.71, 3.76, 3.82, 3.87, 3.93, 3.98, 4.03, 4.09]
u = [7, 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9, 8, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 8.8, 8.9, 9]

plt.minorticks_on()
plt.grid(visible=True, axis='both', which='major')
plt.grid(visible=True, axis='both', which='minor', alpha=0.2)

plt.xlabel('U, В - напряжение')
plt.ylabel("$\omega$, рад/с - частота колебаний")
plt.title('''График зависимости $\omega(U)$''', fontsize=10)


plt.plot(u, w, color='pink', markersize=10)
plt.scatter(7.944329018, 3.52, color='orange')
plt.legend(['$\omega(U)$', 'резонансная частота возбуждения'])

plt.show()