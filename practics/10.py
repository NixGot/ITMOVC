import numpy as np
from matplotlib import pyplot as plt



# def smooth(array, a):
#     res = array
#     ar = np.array([array[0] for i in range(a)])
#     data = np.concatenate([ar, array])
#     for i, el in enumerate(array):
#         c = el
#         for j in range(1, a):
#             c += data[i + j]
        
#         res[i] = c/a
#     return res

def smooth(array, a):
    res = array
    ar = np.array([array[0] for i in range(a)])
    data = np.concatenate([ar, array])
    for i, el in enumerate(array):
        res[i] = np.mean(data[i:i+a])
    return res

data = np.random.rand(2000).copy()
plt.plot(np.arange(len(data)), data)
plt.plot(np.arange(len(data)), smooth(data, 100))
plt.show()