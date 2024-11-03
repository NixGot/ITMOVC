import numpy as np
from time import time
import matplotlib.pyplot as plt
from math import pi
from scipy.constants import h, c, k


# lst = [i for i in range(1000000)]
# np_lst = np.array(lst)
# t = time()
# np_lst * 5
# print(time() - t)
# t = time()
# for n, i in enumerate(lst):
#     lst[n] = lst[n] * 5
# print(time() - t)

# t = time()
# x = np.arange(0, 1000000, 1, dtype=int)
# print(time() - t)
# t = time()
# x = [i for i in range(1000000)]
# print(time() - t)

# x = np.linspace(0, 10, 7, endpoint=False, retstep=True)
# print(x)

# x = np.linspace(0, 3.14, 1000, dtype=float)
# print(np.sin(x))

# x = np.linspace(-pi, pi, 70, dtype=float)
# y = np.sin(x)
# plt.plot(x, y ** 2)
# plt.show()

R = 1
x1 = np.linspace(-R, R, 100, dtype=float)
y1 = np.sqrt(R - x1 ** 2)
y2 = -np.sqrt(R - x1 ** 2)
x2 = np.linspace(0.42, 1.58, 100, dtype=float)
y3 = -50 * x2 ** 2 + 100 * x2 - 32.26
plt.plot(x1, y1)
plt.plot(x1, y2)
plt.plot(x1 + 2, y1)
plt.plot(x1 + 2, y2)
plt.plot(x2, y3)
plt.show()



# def f_plank(l, T):
#     return (2 * h * c ** 2) / ((l) ** 5) / (np.exp(h * c/(l * k * T)) - 1)


# L = np.linspace(1e-17, 5e-5, 1000)
# T = {'SUN': 2800, 'HUMAN': 36, 'MOUSE': 42}
# for i in list(T.keys()):
#     mx = np.max(f_plank(L, (T[i] + 273)))
#     plt.plot(L, f_plank(L, (T[i] + 273))/mx)
# plt.show()

# T = np.linspace(270, 370, 50)
# for i in T:
#     plt.plot(L, f_plank(L, i))
plt.show()

# d = {'12': 5, '45': 16}
# print(list(d.keys()))

