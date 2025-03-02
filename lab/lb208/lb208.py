from matplotlib import pyplot as plt
import numpy as np



plt.minorticks_on()
plt.grid(visible=True, axis='both', which='major')
plt.grid(visible=True, axis='both', which='minor', alpha=0.2)


a = -2.784318215
b = -0.072792886
x = [0.4, 1.3, 1.7, 2.4, 3.0, 3.7, 4.3, 5.0, 5.6, 6.2, 7.2, 8.3, 9.2, 10.2, 11.5, 12.7, 14.7, 15.4, 17.4, 19.2, 20.0]
y = [-2.79, -2.85, -2.90, -2.96, -3.01, -3.06, -3.11, -3.16, -3.20, -3.25, -3.33, -3.39,-3.46, -3.54, -3.62, -3.71, -3.81, -3.92, -4.04, -4.18 , -4.25]
plt.plot(x, y, marker='.', color='black')
plt.plot([0, 21], [a, a+20*b], color='pink')


plt.legend(['X(t)', 'аппроксимация'])
plt.xlabel('$время, с$')
plt.ylabel('$Величина \ X$')
plt.title('график зависимости X(t)')
plt.show()