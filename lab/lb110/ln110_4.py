from matplotlib import pyplot as plt
import numpy as np


a1 = [2.8, 3, 3.8, 4.6, 5.6, 6.4, 9, 17.8, 19, 19, 16.4, 8.4, 6.6, 4.8, 4.2, 3.4, 2.8, 2.6, 2.2, 1.8, 1.8]
a2 = [2.4, 2.6, 3, 3.4, 4, 4.4, 5, 7.6, 10.6, 10.8, 7.6, 4.8, 4, 3.8, 3, 2.8, 2.4, 2, 1.8, 1.8, 1.8]
a3 = [1.8, 2, 2, 2.2, 2.6, 2.8, 3.2, 3.4, 3.6, 3.4, 3.2, 3, 2.6, 2.4, 2.2, 2, 1.8, 1.6, 1.4, 1.4, 1.2]
u = [7, 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9, 8, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 8.8, 8.9, 9]

plt.minorticks_on()
plt.grid(visible=True, axis='both', which='major')
plt.grid(visible=True, axis='both', which='minor', alpha=0.2)

plt.xlabel('$\omega$, рад/с - частота колебаний')
plt.ylabel("a - амплитуда")
plt.title('''График АЧХ для $a(\omega)$''', fontsize=10)


plt.plot(u, a1)
plt.plot(u, a2)
plt.plot(u, a3)
plt.legend(['$I_T = 0 mA$', '$I_T = 200 mA$', '$I_T = 400 mA$'])

plt.show()