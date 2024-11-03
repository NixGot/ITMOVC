from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


plt.minorticks_on()
plt.grid(visible=True, axis='both', which='major')
plt.grid(visible=True, axis='both', which='minor', alpha=0.2)

date = ['1994-04-15', '1994-05-20', '1994-06-25', '1994-09-06', '1994-11-16', '1995-01-10', '1995-02-20', '1995-03-30', '1995-04-20', '1996-10-30','1998-1-15' , '1999-03-30', '1999-04-15', '1999-06-15', '2000-01-30']
votesy = [34, 27, 31, 30, 31, 19, 15, 14, 15, 36, 25, 8, 8, 7 , 15]
votesn = [66, 73, 69, 70, 69, 81, 85, 86, 85, 64, 75, 92, 92, 93, 85]

ser1 = pd.Series(date)
ser2 = pd.Series(votesy)
ser3 = pd.Series(votesn)
date = pd.to_datetime(ser1)
a1, b1 = np.polyfit(date.astype(np.int64), ser2, 1)
a2, b2 = np.polyfit(date.astype(np.int64), ser3, 1)
plt.plot(ser1, ser2, 'g')
plt.plot(ser1, ser3, 'r')
plt.xticks(rotation=45)
plt.xlabel('дата')
plt.ylabel('Процент от проголосовавших, %')
plt.legend(['за', 'против'])
yy = [a1*i + b1 for i in date.astype(np.int64)]
yy = np.array(yy)
yn = [a2*i + b2 for i in date.astype(np.int64)]
yn = np.array(yn)
plt.plot(ser1, yy, 'g', alpha=0.5)
plt.plot(ser1, yn, 'r', alpha=0.5)
plt.show()
 