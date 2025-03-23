from matplotlib import pyplot as plt
import numpy as np



plt.minorticks_on()
plt.grid(visible=True, axis='both', which='major')
plt.grid(visible=True, axis='both', which='minor', alpha=0.2)


x = [0.203, 0.392, 1.344, 1.580, 2.159, 2.159, 3.518, 4.081, 5.001, 5.256]
y = [5.32, 6.69, 6.88, 6.56, 6.87, 6.94, 7.25, 7.33, 7.71, 7.82]
plt.scatter(x, y, marker='.', color='black')
plt.plot([0, 5.5], [0.265047517*0 + 6.3, 0.265047517*5.5 + 6.3], color='pink')


plt.legend(['$R_H(P)$', 'аппроксимация'])
plt.xlabel('$Мощность \ теплового \ потока, \ Вт$')
plt.ylabel('$Сопротивление \ R_H, \ Ом$')
plt.title('график зависимости $R_H(P)$')
plt.show()