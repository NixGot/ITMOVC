from matplotlib import pyplot as plt
import numpy as np


plt.minorticks_on()
plt.grid(visible=True, axis='both', which='major')
plt.grid(visible=True, axis='both', which='minor', alpha=0.2)


t = [0.031905128, 0.035556728, 0.040228328, 0.045919928, 0.052631528, 0.060363128]
gr = [2.542, 2.796, 3.223, 3.649, 4.194, 4.815]
dat = np.stack((t, gr), axis=0)
a = -0.030038673
b = 80.26755477
plt.plot(dat[0], dat[1], color='blue', linewidth=1, marker=".")
plt.plot([0.03, 0.065], [a + b * 0.03, a + b * 0.065], color='purple', linewidth=0.5)



plt.xlabel('I, $кг \cdot м^2$ - момент инерции маятника')
plt.ylabel("$T^2$, $c^2$ - квадрат периода колебаний")
plt.title('''Зависимость квадрата периода кобеланий от момента инерции''', fontsize=10)
plt.legend(['Зависимоть $T^2(I)$ (эксп)','Аппроксимация графика'])
plt.show()