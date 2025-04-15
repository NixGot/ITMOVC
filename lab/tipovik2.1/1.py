from random import random, randint
from matplotlib import pyplot as plt
import numpy as np
from math import log


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
plt.suptitle('Метод прямоугольников, левая граница', fontsize=15)
for i, n in enumerate([4, 8, 16]):
    plt.subplot(2, 2, 1+i)
    plt.minorticks_on()
    plt.grid(visible=True, axis='both', which='major')
    plt.grid(visible=True, axis='both', which='minor', alpha=0.2)
    plt.title(f'n={n}')
    data = gen_delta(0, 1, n, cog=1).copy()
    for i in range(len(data)-1):
        x = np.array([data[i], data[i+1]])
        f = 2**data[i]
        y1 = [f, f]
        y2 = 0
        plt.fill_between(x, y1, y2)
    plt.plot(np.linspace(0, 1, 100), 2**np.linspace(0, 1, 100), color='red')
plt.show()


#прямоугольник правая
plt.suptitle('Метод прямоугольников, правая граница', fontsize=15)
for i, n in enumerate([4, 8, 16]):
    plt.subplot(2, 2, 1+i)
    plt.minorticks_on()
    plt.grid(visible=True, axis='both', which='major')
    plt.grid(visible=True, axis='both', which='minor', alpha=0.2)
    plt.title(f'n={n}')
    data = gen_delta(0, 1, n, cog=1).copy()
    for i in range(len(data)-1):
        x = np.array([data[i], data[i+1]])
        f = 2**data[i+1]
        y1 = [f, f]
        y2 = 0
        plt.fill_between(x, y1, y2)
    plt.plot(np.linspace(0, 1, 100), 2**np.linspace(0, 1, 100), color='red')
plt.show()

#прямоугольник середина
plt.suptitle('Метод прямоугольников, середина', fontsize=15)
for i, n in enumerate([4, 8, 16]):
    plt.subplot(2, 2, 1+i)
    plt.minorticks_on()
    plt.grid(visible=True, axis='both', which='major')
    plt.grid(visible=True, axis='both', which='minor', alpha=0.2)
    plt.title(f'n={n}')
    data = gen_delta(0, 1, n, cog=1).copy()
    for i in range(len(data)-1):
        x = np.array([data[i], data[i+1]])
        f = 2**((data[i]+data[i+1])/2)
        y1 = [f, f]
        y2 = 0
        plt.fill_between(x, y1, y2)
    plt.plot(np.linspace(0, 1, 100), 2**np.linspace(0, 1, 100), color='red')
plt.show()


#прямоугольник случайная
plt.suptitle('Метод прямоугольников, случайная граница', fontsize=15)
for i, n in enumerate([4, 8, 16]):
    plt.subplot(2, 2, 1+i)
    plt.minorticks_on()
    plt.grid(visible=True, axis='both', which='major')
    plt.grid(visible=True, axis='both', which='minor', alpha=0.2)
    plt.title(f'n={n}')
    data = gen_delta(0, 1, n, cog=1).copy()
    for i in range(len(data)-1):
        x = np.array([data[i], data[i+1]])
        f = 2**(data[i]+random()*(data[i+1]-data[i]))
        y1 = [f, f]
        y2 = 0
        plt.fill_between(x, y1, y2)
    plt.plot(np.linspace(0, 1, 100), 2**np.linspace(0, 1, 100), color='red')
plt.show()


#трапеция
plt.suptitle('Метод трапеций', fontsize=15)
for i, n in enumerate([4, 8, 16]):
    plt.subplot(2, 2, 1+i)
    plt.minorticks_on()
    plt.grid(visible=True, axis='both', which='major')
    plt.grid(visible=True, axis='both', which='minor', alpha=0.2)
    plt.title(f'n={n}')
    data = gen_delta(0, 1, n, cog=1).copy()
    for i in range(len(data)-1):
        x = np.array([data[i], data[i+1]])
        y1 = [2**data[i], 2**data[i+1]]
        y2 = 0
        plt.fill_between(x, y1, y2)
    plt.plot(np.linspace(0, 1, 100), 2**np.linspace(0, 1, 100), color='red')
plt.show()



#Симпсон
plt.suptitle('Метод Симпсона', fontsize=15)
for i, n in enumerate([4, 8, 16]):
    plt.subplot(2, 2, 1+i)
    plt.minorticks_on()
    plt.grid(visible=True, axis='both', which='major')
    plt.grid(visible=True, axis='both', which='minor', alpha=0.2)
    plt.title(f'n={n}')
    data = gen_delta(0, 1, n, cog=1).copy()
    for i in range(0, len(data)-2, 2):
        poly = np.polyfit([data[i], data[i+1], data[i+2]], [2**data[i], 2**data[i+1], 2**data[i+2]], 2)
        x = np.linspace(data[i], data[i+2], num=100)
        y1 = poly[0]*x**2 + poly[1]*x + poly[2]
        y2 = 0
        plt.fill_between(x, y1, y2)
    plt.plot(np.linspace(0, 1, 100), 2**np.linspace(0, 1, 100), color='red')
plt.show()



I = 2**1/log(2)-2**0/log(2)

plt.suptitle('Графики зависимости отклонения от n', fontsize=15)
#прямоугольник левая

plt.subplot(2, 3, 1)
plt.minorticks_on()
plt.grid(visible=True, axis='both', which='major')
plt.grid(visible=True, axis='both', which='minor', alpha=0.2)
plt.title(f'прямоугольник левая')

print('Площади для метода прямоугольника, где \ksi - левая граница')
d = []
for i, n in enumerate([1, 2, 4, 8, 16, 32, 64, 128]):
    S = 0
    data = gen_delta(0, 1, n, cog=1).copy()
    for i in range(len(data)-1):
        S += (data[i+1] - data[i])*2**data[i]
    d.append(abs(I-S))
    print(f'S({n}) = {S}')
plt.plot([1, 2, 4, 8, 16, 32, 64, 128], d)

# #прямоугольник правая

plt.subplot(2, 3, 2)
plt.minorticks_on()
plt.grid(visible=True, axis='both', which='major')
plt.grid(visible=True, axis='both', which='minor', alpha=0.2)
plt.title(f'прямоугольник правая')

print('Площади для метода прямоугольника, где \ksi - правая граница')
d = []
for i, n in enumerate([1, 2, 4, 8, 16, 32, 64, 128]):
    S = 0
    data = gen_delta(0, 1, n, cog=1).copy()
    for i in range(len(data)-1):
        S += (data[i+1] - data[i])*2**data[i+1]
    d.append(abs(I-S))
    print(f'S({n}) = {S}')
plt.plot([1, 2, 4, 8, 16, 32, 64, 128], d)

# #прямоугольник середина

plt.subplot(2, 3, 3)
plt.minorticks_on()
plt.grid(visible=True, axis='both', which='major')
plt.grid(visible=True, axis='both', which='minor', alpha=0.2)
plt.title(f'прямоугольник середина')

print('Площади для метода прямоугольника, где \ksi - середина')
d = []
for i, n in enumerate([1, 2, 4, 8, 16, 32, 64, 128]):
    S = 0
    data = gen_delta(0, 1, n, cog=1).copy()
    for i in range(len(data)-1):
        S += (data[i+1] - data[i])*2**((data[i] + data[i+1])/2)
    d.append(abs(I-S))
    print(f'S({n}) = {S}')
plt.plot([1, 2, 4, 8, 16, 32, 64, 128], d)

# #прямоугольник случайная

plt.subplot(2, 3, 4)
plt.minorticks_on()
plt.grid(visible=True, axis='both', which='major')
plt.grid(visible=True, axis='both', which='minor', alpha=0.2)
plt.title(f'прямоугольник случайная')

print('Площади для метода прямоугольника, где \ksi - случайное')
d = []
for i, n in enumerate([1, 2, 4, 8, 16, 32, 64, 128]):
    S = 0
    data = gen_delta(0, 1, n, cog=1).copy()
    for i in range(len(data)-1):
        S += (data[i+1] - data[i])*2**(random()*(data[i+1]-data[i])+data[i])
    d.append(abs(I-S))
    print(f'S({n}) = {S}')
plt.plot([1, 2, 4, 8, 16, 32, 64, 128], d)


# #трапеция

plt.subplot(2, 3, 5)
plt.minorticks_on()
plt.grid(visible=True, axis='both', which='major')
plt.grid(visible=True, axis='both', which='minor', alpha=0.2)
plt.title(f'трапеция')

print('Площади для метода трапеции')
d = []
for i, n in enumerate([1, 2, 4, 8, 16, 32, 64, 128]):
    S = 0
    data = gen_delta(0, 1, n, cog=1).copy()
    for i in range(len(data)-1):
        S += (2**data[i] + 2**data[i+1])*(data[i+1]-data[i])/2
    d.append(abs(I-S))
    print(f'S({n}) = {S}')
plt.plot([1, 2, 4, 8, 16, 32, 64, 128], d)



# #Симпсон

plt.subplot(2, 3, 6)
plt.minorticks_on()
plt.grid(visible=True, axis='both', which='major')
plt.grid(visible=True, axis='both', which='minor', alpha=0.2)
plt.title(f'Метод Симпсона')

print('Площади для метода Симпсона')
d = []
for i, n in enumerate([1, 2, 4, 8, 16, 32, 64, 128]):
    S = 0
    data = gen_delta(0, 1, n, cog=1).copy()
    for i in range(len(data)-1):
        S += (2**data[i] + 2**data[i+1] + 4*2**((data[i]+data[i+1])/2))*(data[i+1]-data[i])/6
    d.append(abs(I-S))
    print(f'S({n}) = {S}')
plt.plot([1, 2, 4, 8, 16, 32, 64, 128], d)

plt.show()
