import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# func1 = lambda x1,a,b: a*np.exp(b*x1)
# func2 = lambda x1, a, b, c, d: a*np.exp(b*x1) + c*np.exp(d*x1)
# func3 = lambda x1, a, b, c, d, e, f: a*np.exp(b*x1) + c*np.exp(d*x1) + e*np.exp(f*x1)
# guess1 = np.array([0.3, -1/0.5])
# guess2 = np.array([0.3, -1/0.5, 0.3, -1/10])
# guess3 = np.array([0.3, -1/0.5, 0.3, -1/5, 0.3, -1/20])

# length  = 20

# x = np.linspace(1, 10, length)
# y = x**2

# func = func2
# guess = guess2
# popt, pcov = curve_fit(func,  x, y) 
# y_pred = func(x, *popt)

# times = []
# for n, i in enumerate(popt):       
#     if n % 2 != 0:
#         t = -1/i
#         times.append(t)
# print(times)

# noise = np.random.normal(0, 0.1, 100)

# plt.plot(noise)
# plt.show()

# def test_curvefit(foo, x, y, par: list) -> bool:
#     popt, pcow = curve_fit()
#     if abs((par[2] - popt[2])/popt[2]) < 0.01:
#         return 1
#     else:
#         return 0

# a, b, T = 0, 1, 100

# end = 400
# step = 1

# x = np.arange(0 , end, step)
# exp = exp1(x, a, b, t1)
# noise = np.random.normal(0, 0.01, np.shape(x)[0])

# t1_rand = np.random.uniform(1, 100, 10)
# a_rand = np.random.uniform(0, 10, 10)
# b_rand = np.random.uniform(0.1, 10, 10)

# fails = 0
# for i in range (10):
#     exp = exp1(x, a_rand[i], b_rand[i], t1_rand[i])
#     signal = exp + np.random.normal(0, 0.1, np.shape(x)[0])
#     result = test_curvefit(exp1, x, signal, [a_rand[i], b_rand[i], t1_rand[i]])
#     if result == 0:
#         fails += 1

# signal = exp + noise
# plt.yscale('log')
# plt.plot(exp)
# plt.plot(signal)
# plt.show()

#  потом можно глянуть в папке практики