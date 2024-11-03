import numpy as np
import matplotlib.pyplot as plt
import os


path = 'spectral_groups/NL_8types/'
name_data = os.listdir(path)
for i in name_data:
    data = np.loadtxt(path + i, comments='#', delimiter='	')
    print(f'{i[:i.index('.')]+'nm'} maxL = ',data.T[0][np.argmax(data.T[1])])
    plt.plot(data[:, 0], data[:, 1]/max(data.T[1]))

names = [i[:i.index('.')]+'nm' for i in name_data]
plt.legend(names)

plt.show()
