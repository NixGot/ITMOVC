from matplotlib import pyplot as plt
import numpy as np


a = [1.49, 1.66, 1.86, 2.13, 2.49, 3.01, 3.81, 5.19, 7.96, 13.85, 12.89, 7.31, 4.77, 3.49, 2.74, 2.24, 1.89, 1.63, 1.43, 1.28, 1.15]
u = [7, 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9, 8, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 8.8, 8.9, 9]

plt.minorticks_on()
plt.grid(visible=True, axis='both', which='major')
plt.grid(visible=True, axis='both', which='minor', alpha=0.2)

plt.xlabel('$\omega$, рад/с - частота колебаний')
plt.ylabel("a - амплитуда")
plt.title('''Теоретический график $a(\omega)$ при $I_T = 200 mA$''', fontsize=10)


plt.plot(u, a)
plt.legend(['$a(\omega)$'])

plt.show()