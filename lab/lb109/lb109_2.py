from matplotlib import pyplot as plt
import numpy as np



plt.minorticks_on()
plt.grid(visible=True, axis='both', which='major')
plt.grid(visible=True, axis='both', which='minor', alpha=0.2)

y = [9.1204, 11.2225, 13.93777778, 17.16721111, 21.40604444, 25.56987778, 30.3601]
x = [0.0036, 0.0064, 0.01, 0.0144, 0.0196, 0.0256, 0.0324]
plt.plot(x, y, marker='.', color='black')


plt.legend(['$T^2(l^2)$'])
plt.xlabel('$Квадрат \ расстояния \ грузов \ от \ центра, м$')
plt.ylabel('$Квадрат \ периода \ колебаний \ системы, с:2$')
plt.title('График  зависимости $T^2(l^2)$')
plt.show()