from microbit import *
import radio
radio.on()
radio.config(channel = 42)
radio.config(power=7)
sw_a = 0
sw_b = 0
sw_8 = 0
while 1:
    x = radio.receive()
    if x != None:
        print(x)
    if button_a.is_pressed():
        while button_a.is_pressed():
            sleep(10)
        sw_a += 1
        if sw_a > 10:
            sw_a = 1
        msg = 'L'+str(sw_a)
        radio.send(msg)
    elif button_b.is_pressed():
        while button_b.is_pressed():
            sleep(10)
        sw_b += 1
        if sw_b > 10:
            sw_b = 1
        msg = 'S'+str(sw_b)
        radio.send(msg)
    if not pin8.read_digital():
        while not pin8.read_digital():
            sleep(10)
        sw_8 += 1
        if sw_8 > 10:
            sw_8 = 1
        msg = "H"+str(sw_8)
        radio.send(msg)

