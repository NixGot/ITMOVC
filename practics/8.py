import os
import matplotlib.pyplot as plt
import numpy as np

# path = 'thorlabs_spectral_sensitivity'
# f_name = '/spectrum_20241024_144629.csv'
# s_name = '/S130C_sensitivity.txt'

# data = np.loadtxt(path + f_name, delimiter=',', comments='#', skiprows=11, max_rows=41)
# data_s = np.loadtxt(path + s_name, delimiter='	', max_rows=81)
# plt.plot(data[:, 0], data[:, 1]/np.max(data[:, 1]))
# plt.plot(data_s[:, 0], data_s[:, 1]/np.max(data_s[:, 1]))
# x_r = np.arange(400, 800, 10)
# sp1 = np.interp(x_r, data[:, 0], data[:, 1]/np.max(data[:, 1]))
# sp2 = np.interp(x_r ,data_s[:, 0], data_s[:, 1]/np.max(data_s[:, 1]))
# y = sp1 / sp2
# plt.plot(x_r, y/np.max(y))
# plt.show()

path = 'CCD2008/'


name_data = list(filter(lambda x: x[-3:] == 'dat', os.listdir(path)))

data = np.fromfile(f'{path}-60 1 sec.dat', dtype='int16')
sp_x = np.linspace(0, 1, 1024)
print(data)
plt.plot(sp_x, data, linewidth=0.2)
plt.show()