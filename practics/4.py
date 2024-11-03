# def s(n, a):
#     print(a)
#     for i in range(n):
#         print(a)
#         a += 1
#     else:
#         print(a)


# s(5, 0)


# def f(a, n):
#     if n == 0:
#         return a
#     else:
#         print(a)
#         return f(a+1, n-1)
    
# a = 0
# print(f(a, 1000))

# from math import pi, exp, sqrt 


# def gaus(x, m=0, s=2):
#     return exp(-0.5 * ((x - m) / s) ** 2) / (sqrt(2 * pi) * s)

# x = 1.0

# print(gaus(x))

import numpy as np
from math import pi, exp, sqrt 


def gaus(x, m=0, s=2):
    return exp(-0.5 * ((x - m) / s) ** 2) / (sqrt(2 * pi) * s)


rnd = np.random.default_rng()
sp = rnd.integers(low=1, high=10, size=20).copy()
print(sp, '\n', list(filter(lambda x: x>0.01, [gaus(x) for x in sp])))
print(sp, '\n', list(filter(lambda x: x>0.01, map(gaus,sp))))