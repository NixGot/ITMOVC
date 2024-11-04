from matplotlib import pyplot as plt
import numpy as np


plt.minorticks_on()
plt.grid(visible=True, axis='both', which='major')
plt.grid(visible=True, axis='both', which='minor', alpha=0.2)

T13 = [0.852, 0.869, 0.895, 0.943, 1.036, 1.199, 1.493]
T23 = [0.508, 0.517, 0.540, 0.587, 0.666, 0.785, 1.018]
T12 = [0.663, 0.669, 0.682, 0.724, 0.803, 0.935, 1.153]
x = [4.020, 4.082, 4.278, 4.642, 5.248, 6.254, 8.040]
plt.plot(x, T13, marker='.')
plt.plot(x, T23, marker='.')
plt.plot(x, T12, marker='.')
plt.legend(['l = 1/3 $l_{ст}$', 'l = 2/3 $l_{ст}$', 'l = 1/2 $l_{ст}$'])
plt.xlabel('$\dfrac{4\pi^2}{g_{эфф}}, \dfrac{с^2}{м}$')
plt.ylabel('$T^2, с^2$')
plt.title('График зависимости $T^2 \left(\dfrac{4\pi^2}{g_{эфф}}\\right)$')
print(np.polyfit(x, T13, deg=1))
print(np.polyfit(x, T23, deg=1))
print(np.polyfit(x, T12, deg=1))
plt.show()