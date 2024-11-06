import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


func1 = lambda x1,a,b: a*np.exp(b*x1)
func2 = lambda x1, a, b, c, d: a*np.exp(b*x1) + c*np.exp(d*x1)
func3 = lambda x1, a, b, c, d, e, f: a*np.exp(b*x1) + c*np.exp(d*x1) + e*np.exp(f*x1)
guess1 = np.array([0.3, -1/0.5])
guess2 = np.array([0.3, -1/0.5, 0.3, -1/10])
guess3 = np.array([0.3, -1/0.5, 0.3, -1/5, 0.3, -1/20])

length  = 20

x = np.linspace(1, 10, length)
y = x**2

func = func2
guess = guess2
popt, pcov = curve_fit(func,  x, y) 
y_pred = func(x, *popt)

times = []
for n, i in enumerate(popt):       
    if n % 2 != 0:
        t = -1/i
        times.append(t)
print(times)

noise = np.random.normal(0, 0.1, 100)

plt.plot(noise)
plt.show()