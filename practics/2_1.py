from playsound import playsound
from time import sleep, time
import keyboard, math

data = []
bpm = int(input('введите bpm (шаг 1/4) press q; exit press w '))
path = './music/' 
loop = 1

while loop:
    if keyboard.is_pressed('w'):
        loop = 0
    playsound(f'{path}minor.mp3')
    sleep(60/bpm/4)
    playsound(f'{path}major.mp3')
    sleep(60/bpm/4)
    playsound(f'{path}minor.mp3')
    sleep(60/bpm/4)
    playsound(f'{path}major.mp3')
    t = round(time()*1000)
    while True:  
        try: 
            if keyboard.is_pressed('q'):
                data.append((round(time()*1000) - t) - 60/bpm/4*1000)
                print(f'{(round(time()*1000) - t) - 60/bpm/4*1000}ms')
                break 
            elif round(time()*1000) - t == 60/bpm/4*1000:
                break
        except:
            break
    sleep(((t + 60/bpm/4*1000 - round(time()*1000))/1000))
    t = round(time()*1000)
    while True:  
        try:  
            if keyboard.is_pressed('q'):
                data.append(round(time()*1000) - t)
                print(f'{round(time()*1000) - t}ms')
                break
            elif round(time()*1000) - t == 60/bpm/4*1000:
                break
        except:
            break
    sleep(((t + 60/bpm/4*1000 - round(time()*1000))/1000))
res = []
for i in data:
    if i != 0:
        res.append(i)
print(res)