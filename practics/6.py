import numpy as np
from math import pi
from scipy.constants import h, c, k
import matplotlib.pyplot as plt



# def f_plank(l, T):
#     return (2 * h * c ** 2) / ((l) ** 5) / (np.exp(h * c/(l * k * T)) - 1)


# filename = 'np_list.csv'
# l = np.linspace(1e-17, 5e-5, 100)
# t = np.linspace(270, 370, 50)
# I = np.array([f_plank(i, 270) for i in l])
# np.savetxt(filename, np.stack((l, I), axis=0).T, fmt='%.2e', delimiter=';', header='l\tI')

# data = np.loadtxt(filename, comments='#', delimiter=';')
# plt.plot(data[:,0], data[:,1])
# plt.show()

# filename = 'csv_averaging\Led_royalBlue.csv'
# data = np.loadtxt(filename, delimiter=',', skiprows=2, usecols=[0, 1], max_rows=101)
# plt.plot(data[:,0], data[:,1])
# plt.show()

# filename = 'csv_averaging\Led370nm.csv'
# data = np.loadtxt(filename, delimiter=',', skiprows=3, max_rows=301)
# for i in range(1, 7):
#     plt.plot(data[:,0], data[:,i])
# plt.show()

filename = 'csv_averaging\Led280nm.csv'
index_list = np.concatenate([np.array([0], dtype=int), np.arange(1, 20, 2, dtype=int)])
data = np.loadtxt(filename, delimiter=',', skiprows=2, max_rows=301, usecols=index_list)
print(data[:, 0])
for i in range(1, 11):
    plt.plot(data[:,0], data[:,i])
plt.show()
