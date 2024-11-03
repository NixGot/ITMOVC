import numpy as np
import matplotlib.pyplot as plt
import math

def aver_dev(data):
    aver = sum(data)/len(data)
    accum = 0
    for i in data:
        accum += (i - aver) ** 2
    dev = math.sqrt(accum/len(data))
    return(aver, dev)


rnd = np.random.default_rng()
data = rnd.integers(low=1, high=100, size=22).copy()
plt.hist(data, bins=9, color='skyblue', edgecolor='black')
 
plt.xlabel('Баллы')
plt.ylabel('Частота')
plt.title('Распределение баллов')
 
# Display the plot
print(aver_dev(data))
plt.show()