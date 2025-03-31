from matplotlib import pyplot as plt
import numpy as np


plt.minorticks_on()
plt.grid(visible=True, axis='both', which='major')
plt.grid(visible=True, axis='both', which='minor', alpha=0.2)


x = [345,360,375,390,405,420,435,450,465,480,495,510,525,540,555,570,585,600,615,630,645,660,675,690,705,720,735,750,765,780,795,810,825]
y = [219,213,207,203,198,193,189,184,180,176,173,169,165,162,159,156,153,150,147,144,141,139,136,133,131,129,126,124,122,120,118,116,114]
plt.plot(x, np.log(y), marker='.', color='black')
plt.plot([340, 830], [340*(-0.00136)+5.84, 830*(-0.00136)+5.84], color='pink')


plt.legend(['$R_H(P)$', 'аппроксимация'])
plt.xlabel('$Мощность \ теплового \ потока, \ Вт$')
plt.ylabel('$Сопротивление \ R_H, \ Ом$')
plt.title('график зависимости $R_H(P)$')
plt.show()