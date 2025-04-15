from random import random, randint
from matplotlib import pyplot as plt
import numpy as np


def gen_delta(a, b, n, cog=1):
    delt = [a]
    d = (b-a)/n
    if cog == 1:
        for i in range(1, n+1):
            delt.append(a+i*d)
    else:
        p = a
        dt = 0
        for i in range(1, n):
            x = d/3 * random() * randint(-1, 1)
            delt.append(p + x + d)
            p += x + d
            dt += x
        delt.append(b)
    return delt


#прямоугольник левая
for i, n in enumerate([4, 8, 16]):
    plt.subplot(2, 2, 1+i)
    plt.minorticks_on()
    plt.grid(visible=True, axis='both', which='major')
    plt.grid(visible=True, axis='both', which='minor', alpha=0.2)
    data = gen_delta(0, 1, n, cog=1).copy()
    for i in range(len(data)-1):
        x = np.array([data[i], data[i+1]])
        f = 2**data[i]
        y1 = [f, f]
        y2 = 0
        plt.fill_between(x, y1, y2)
plt.show()


#прямоугольник правая
for i, n in enumerate([4, 8, 16]):
    plt.subplot(2, 2, 1+i)
    plt.minorticks_on()
    plt.grid(visible=True, axis='both', which='major')
    plt.grid(visible=True, axis='both', which='minor', alpha=0.2)
    data = gen_delta(0, 1, n, cog=1).copy()
    for i in range(len(data)-1):
        x = np.array([data[i], data[i+1]])
        f = 2**data[i+1]
        y1 = [f, f]
        y2 = 0
        plt.fill_between(x, y1, y2)
plt.show()

#прямоугольник середина
for i, n in enumerate([4, 8, 16]):
    plt.subplot(2, 2, 1+i)
    plt.minorticks_on()
    plt.grid(visible=True, axis='both', which='major')
    plt.grid(visible=True, axis='both', which='minor', alpha=0.2)
    data = gen_delta(0, 1, n, cog=1).copy()
    for i in range(len(data)-1):
        x = np.array([data[i], data[i+1]])
        f = 2**((data[i]+data[i+1])/2)
        y1 = [f, f]
        y2 = 0
        plt.fill_between(x, y1, y2)
plt.show()


#прямоугольник случайная
for i, n in enumerate([4, 8, 16]):
    plt.subplot(2, 2, 1+i)
    plt.minorticks_on()
    plt.grid(visible=True, axis='both', which='major')
    plt.grid(visible=True, axis='both', which='minor', alpha=0.2)
    data = gen_delta(0, 1, n, cog=1).copy()
    for i in range(len(data)-1):
        x = np.array([data[i], data[i+1]])
        f = 2**(data[i]+random()*(data[i+1]-data[i]))
        y1 = [f, f]
        y2 = 0
        plt.fill_between(x, y1, y2)
plt.show()


#трапеция
for i, n in enumerate([4, 8, 16]):
    plt.subplot(2, 2, 1+i)
    plt.minorticks_on()
    plt.grid(visible=True, axis='both', which='major')
    plt.grid(visible=True, axis='both', which='minor', alpha=0.2)
    data = gen_delta(0, 1, n, cog=1).copy()
    for i in range(len(data)-1):
        x = np.array([data[i], data[i+1]])
        y1 = [2**data[i], 2**data[i+1]]
        y2 = 0
        plt.fill_between(x, y1, y2)
plt.show()



#Симпсон
for i, n in enumerate([4, 8, 16]):
    plt.subplot(2, 2, 1+i)
    plt.minorticks_on()
    plt.grid(visible=True, axis='both', which='major')
    plt.grid(visible=True, axis='both', which='minor', alpha=0.2)
    data = gen_delta(0, 1, n, cog=1).copy()
    for i in range(len(data)-1):
        x = np.array([data[i], data[i+1]])
        y1 = [2**data[i], 4*2**((data[i]+data[i+1])/2), 2**data[i+1]]
        y2 = 0
        plt.fill_between(x, y1, y2)
plt.show()