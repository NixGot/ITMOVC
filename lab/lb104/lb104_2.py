from matplotlib import pyplot as plt

#y = 0,0139x + 0.0235
#y = 0,0125x + 0,0350
#y = 0,0197x + 0,0428	
#y = 0,0179x + 0,0606	
#y = 0,0175x + 0,0781
#y = 0,0190x + 0,0966


plt.ylim(0, 0.12)
plt.xlim(0, 0.05)
plt.minorticks_on()
plt.grid(visible=True, axis='both', which='major')
plt.grid(visible=True, axis='both', which='minor', alpha=0.2)

a = 0.011452151	
b = 2.098511169	
R = [0.005929, 0.010404, 0.016129, 0.023104, 0.031329, 0.040804]
I = [0.023519762, 0.035017557, 0.042841547, 0.060637692, 0.078105415, 0.096568712]

plt.plot([0, R[0]], [b, R[0]*a + b], linestyle='dashed', color='red', linewidth=0.5)
plt.plot([R[0], R[-1]], [R[0]*a + b, R[-1]*a + b], color='red', linewidth=0.5)
plt.plot([R[-1], 0.05], [R[-1]*a + b, 0.05*a + b], linestyle='dashed', color=f'red', linewidth=0.5)


plt.scatter(R, I, color='purple', s=8)

# plt.text(R[3]-0.1, I[3]-0.02, 'номер риски', color='blue', fontsize=6)

plt.xlabel('ε, м/с² - угловое ускорение')
plt.ylabel("M, H·м - момент силы натяжения нити")
plt.title('''Эксперементальные точки зависимости момента силы натяжения нити от
           углового ускорения, и их линейные теоретические графики''', fontsize=10)

plt.show()