from matplotlib import pyplot as plt
import numpy as np


y1 = [0.00, 0.02, 0.04, 0.05, 0.07, 0.09, 0.10, 0.12, 0.14, 0.16, 0.17]
y2 = [0.00, 0.09, 0.17, 0.24, 0.32, 0.39, 0.48, 0.58, 0.64, 0.73, 0.82]
y3 = [0.00, 0.25, 0.51, 0.75, 1.03, 1.30, 1.61, 1.91, 2.25, 2.47, 2.94]
x = [0, 1.784666667, 3.569333333, 5.354, 7.138666667, 8.923333333, 10.708, 12.49266667, 14.27733333, 16.062, 17.84666667]
b1 = 0.009476
b2 = 0.045290
b3 = 0.161778

plt.minorticks_on()
plt.grid(visible=True, axis='both', which='major')
plt.grid(visible=True, axis='both', which='minor', alpha=0.2)

plt.xlabel('$\omega$, рад/с - частота вращения маховика')
plt.ylabel("t, с - время")
plt.title('''Зависимость функции $f(t) = ln(A_0/A_k)$''', fontsize=10)


plt.plot([0, 18], [0, 18*b1], color='blue', markersize=10)

plt.plot([0, 18], [0, 18*b2], color='red', markersize=10)

plt.plot([0, 18], [0, 18*b3], color='orange', markersize=10)
plt.legend(['$I_T = 0 mA$', '$I_T = 200 mA$', '$I_T = 400 mA$'])

plt.show()