from microbit import *
from iled4 import *
from IRM import *
# import music

pin12.set_pull(pin12.PULL_UP)
d = IRM()
f = iled4()
key_number = {12: 0, 16: 1, 17: 2, 18: 3, 20: 4, 21: 5, 22: 6, 24: 7, 25: 8, 26: 9}


digit = 0
number0 = 0
number1 = 0
number2 = 0
number3 = 0
password = 0
mode = None
def servo(pin,degrees):
    degrees=max(0, min(degrees, 180))
    duty= degrees / 180 * 102 + 25
    pin.write_analog(duty)

servo(pin8,0)
while 1:
    key = d.get(pin12)
    if key != -1:
        print("password" + str(password))
        #music.pitch(2000, 100)
        if digit >= 4:
            digit = 0
        if key in key_number:
            if digit == 0:
                number0 = key_number[key]
                digit += 1
            elif digit == 1:
                number1 = key_number[key]
                digit += 1
            elif digit == 2:
                number2 = key_number[key]
                digit += 1
            elif digit == 3:
                number3 = key_number[key]
                digit += 1
        password = number0 * 1000 + number1 * 100 + number2 * 10 + number3
        if key == 0:
            if password == 1234:
                print("Servo")
                servo(pin8, 180)
                sleep(500)
                # music.pitch(2000, 100)
                display.show(Image.YES)
                sleep(500)
                display.clear()
            else:
                display.show(Image.NO)
                # music.play(music.DADADADUM)
                sleep(500)
                display.clear()
        elif key == 13:
            servo(pin8, 0)
            digit = 0
            number0 = 0
            number1 = 0
            number2 = 0
            number3 = 0
            password = 0
        else:
            pass
    else:
        pass
    f.print(number0 * 1000 + number1 * 100 + number2 * 10 + number3)
    f.update_display()
