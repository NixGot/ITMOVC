from matplotlib import pyplot as plt
import numpy as np


fig, ax = plt.subplots(figsize=(7, 4))

plt.minorticks_on()
plt.grid(visible=True, axis='both', which='major')
plt.grid(visible=True, axis='both', which='minor', alpha=0.2)

y = [0.0885, 0.0589, 0.0260, 0, -0.0487, -0.0801, -0.1028]
x = [3*np.pi/2, np.pi, np.pi/2, 0, -np.pi/2, -np.pi, -3*np.pi/2]
plt.plot(x, y, marker='.', color='black')
custom_ticks = x
custom_tick_labels = ['$\pi/2$', '$\pi$', '$3\pi/2$', '$0$','$-\pi/2$', '$-\pi$', '$-3\pi/2$']

plt.plot(x, [np.polyfit(x, y, deg=1)[0] * i + np.polyfit(x, y, deg=1)[1] for i in x], color='pink')
print(np.polyfit(x, y, deg=1))

ax.set_xticks(custom_ticks)
ax.set_xticklabels(custom_tick_labels)

plt.legend(['$M(\phi)$', 'аппроксимация'])
plt.xlabel('$Угол \ отклонения \ \phi, рад$')
plt.ylabel('$Момент силы М, Н \cdot м$')
plt.title('График зависимости $M(\phi)$')
plt.show()