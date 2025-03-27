from matplotlib import pyplot as plt
import numpy as np



plt.minorticks_on()
plt.grid(visible=True, axis='both', which='major')
plt.grid(visible=True, axis='both', which='minor', alpha=0.2)

y = [6.9696, 7.858677778, 9.3025, 12.48444444, 16.34854444]
x = [0, 0.0009, 0.0036, 0.0081, 0.0144]
plt.plot(x, y, marker='.', color='black')


plt.legend(['$T^2(l^2)$'])
plt.xlabel('$Квадрат \ расстояния \ оси \ от \ центра, м$')
plt.ylabel('$Квадрат \ периода \ колебаний \ системы, с^2$')
plt.title('График  зависимости $T^2(l^2)$')
plt.show()