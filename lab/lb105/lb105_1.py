from matplotlib import pyplot as plt
import numpy as np


plt.minorticks_on()
plt.grid(visible=True, axis='both', which='major')
plt.grid(visible=True, axis='both', which='minor', alpha=0.2)


t = [0, 47.34, 98.14, 155.97, 218.57, 293.88]
gr = [30, 25, 20, 15, 10, 5]
dat = np.stack((t, gr), axis=0)
plt.plot(dat[0], dat[1], color='blue', linestyle='dashed', linewidth=0.5, marker=".")
plt.plot([0, t[-1]], [30, 5], color='green', linewidth=0.5)



plt.xlabel('t, с - время')
plt.ylabel("A, ° - амплитуда, по шкале маятника в градусах")
plt.title('''Зависимость амплитуды маятника от времени''', fontsize=10)
# plt.text(180, 20, 'Идеальная зависимость при сухом трении', color='green', fontsize=6)
# plt.text(180, 18, 'Эксперементальная зависимость', color='blue', fontsize=6)
plt.legend(['Идеальная зависимость при сухом трении', 'Эксперементальная зависимость'])
plt.show()