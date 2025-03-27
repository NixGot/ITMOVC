from matplotlib import pyplot as plt
import numpy as np

T = 1.78
a1 = [19, 18.6, 18.2, 18, 17.8, 17.4, 17.2, 16.8, 16.6, 16.2, 16]
a2 = [19, 17.4, 16, 15, 13.8, 12.8, 11.8, 10.6, 10, 9.2, 8.4]
a3 = [19, 14.8, 11.4, 9, 6.8, 5.2, 3.8, 2.8, 2, 1.6, 1]
data1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
data2 = data1*T

fig, ax1 = plt.subplots()


plt.title('''Зависимость амплитуды от времени A(t)''', fontsize=10)
color1 = 'green'
color2 = 'pink'
color3 =  'red'
ax1.set_xlabel('T, c - период колебания')
ax1.set_ylabel('A, ед. - амплитуда ')
ax1.plot(data1, a1, color=color1)
ax1.plot(data1, a2, color=color2)
ax1.plot(data1, a3, color=color3)


ax2 = ax1.twiny()

ax2.set_xlabel('t, c - время')


ax2.plot(data2, a1, color=color1)
ax2.plot(data2, a2, color=color2)
ax2.plot(data2, a3, color=color3)
plt.legend(['$I_T = 0 mA$', '$I_T = 200 mA$', '$I_T = 400 mA$'])

fig.tight_layout()
plt.show()