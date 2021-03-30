from lib.keyDetect import keyDetect
import keyboard
import os

kd = keyDetect()
page = ['Hello', 'Hi']
choose = 0
# init screen
os.system('cls')
for i in range(len(page)):
        print('>' if i == choose else '', page[i])
while True:
    key = kd.getKey()
    # print(key)
    if key == 'up':
        if choose > 0:
            choose -= 1
    elif key == 'down':
        if choose < len(page)-1:
            choose += 1
    elif key == 'space':
        print(f"you choose {page[choose]}")
        break
    if key != None:
        os.system('cls')
        for i in range(len(page)):
            print('>' if i == choose else '', page[i])