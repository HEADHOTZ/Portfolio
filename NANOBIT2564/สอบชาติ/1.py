from microbit import *
import neopixel
import gc
gc.collect()
np = neopixel.NeoPixel(pin8, 12)
enter = pin12
esc = pin14
num0 = 0
num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0
num6 = 0
num7 = 0
num8 = 0
num9 = 0
num10 = 0
num11 = 0
num = [num0,num1,num2,num3,num4,num5,num6,num7,num8,num9,num10,num11]
color0 = [(255,0,0),(255,242,0),(0,255,0),(0,0,255),(0,255,255),(64,0,64),(255,255,255),(0,0,0)]
color = ""
i = 0
while 1:
    if not enter.read_digital():
        while not enter.read_digital():
            sleep(10)
        i += 1
        if i > 11:
            i = 0
    if not esc.read_digital():
        while not esc.read_digital():
            sleep(10)
        num[i] += 1
        if num[i] > 7:
            num[i] = 0
    if num[i] == 0:
        color = "RED"
    elif num[i] == 1:
        color = "YELLOW"
    elif num[i] == 2:
        color = "GREEN"
    elif num[i] == 3:
        color = "BLUE"
    elif num[i] == 4:
        color = "SKY"
    elif num[i] == 5:
        color = "PURPLE"
    elif num[i] == 6:
        color = "WHITE"
    elif num[i] == 7:
        color = "BLACK"
    if i == 0:
        display.show(num[0] + 1)
        np[0] = color0[num[0]]
        np.show()
        sleep(10)
        np[0] = (0, 0, 0)
        np.show()
        sleep(10)
        print("LED = 0 " + " Color = " + color)
    if i == 1:
        display.show(num[1] + 1)
        np[1] = color0[num[1]]
        np.show()
        sleep(10)
        np[1] = (0, 0, 0)
        np.show()
        sleep(10)
        print("LED = 1 " + " Color = " + color)
    if i == 2:
        display.show(num[2] + 1)
        np[2] = color0[num[2]]
        np.show()
        sleep(10)
        np[2] = (0, 0, 0)
        np.show()
        sleep(10)
        print("LED = 2 " + " Color = " + color)

    if i == 3:
        display.show(num[3] + 1)
        np[3] = color0[num[3]]
        np.show()
        sleep(10)
        np[3] = (0, 0, 0)
        np.show()
        sleep(10)
        print("LED = 3 " + " Color = " + color)
    if i == 4:
        display.show(num[4] + 1)
        np[4] = color0[num[4]]
        np.show()
        sleep(10)
        np[4] = (0, 0, 0)
        np.show()
        sleep(10)
        print("LED = 4 " + " Color = " + color)
    if i == 5:
        display.show(num[5] + 1)
        np[5] = color0[num[5]]
        np.show()
        sleep(10)
        np[5] = (0, 0, 0)
        np.show()
        sleep(10)
        print("LED = 5 " + " Color = " + color)
    if i == 6:
        display.show(num[6] + 1)
        np[6] = color0[num[6]]
        np.show()
        sleep(10)
        np[6] = (0, 0, 0)
        np.show()
        sleep(10)
        print("LED = 6 " + " Color = " + color)
    if i == 7:
        display.show(num[7] + 1)
        np[7] = color0[num[7]]
        np.show()
        sleep(10)
        np[7] = (0, 0, 0)
        np.show()
        sleep(10)
        print("LED = 7 " + " Color = " + color)
    if i == 8:
        display.show(num[8] + 1)
        np[8] = color0[num[8]]
        np.show()
        sleep(10)
        np[8] = (0, 0, 0)
        np.show()
        sleep(10)
        print("LED = 8 " + " Color = " + color)
    if i == 9:
        display.show(num[9] + 1)
        np[9] = color0[num[9]]
        np.show()
        sleep(10)
        np[9] = (0, 0, 0)
        np.show()
        sleep(10)
        print("LED = 9 " + " Color = " + color)
    if i == 10:
        display.show(num[10] + 1)
        np[10] = color0[num[10]]
        np.show()
        sleep(10)
        np[10] = (0, 0, 0)
        np.show()
        sleep(10)
        print("LED = 10 " + " Color = " + color)
    if i == 11:
        display.show(num[11] + 1)
        np[11] = color0[num[11]]
        np.show()
        sleep(10)
        np[11] = (0, 0, 0)
        np.show()
        sleep(10)
        print("LED = 11 " + " Color = " + color)
    np[0] = color0[num[0]]
    np[1] = color0[num[1]]
    np[2] = color0[num[2]]
    np[3] = color0[num[3]]
    np[4] = color0[num[4]]
    np[5] = color0[num[5]]
    np[6] = color0[num[6]]
    np[7] = color0[num[7]]
    np[8] = color0[num[8]]
    np[9] = color0[num[9]]
    np[10] = color0[num[10]]
    np[11] = color0[num[11]]
    np.show()
