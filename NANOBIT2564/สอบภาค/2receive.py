from microbit import *
import radio

radio.on()
radio.config(channel=42)
radio.config(power=7)


def servo(pin, degrees):
    degrees = max(0, min(degrees, 180))
    duty = degrees / 180 * 102 + 25
    pin.write_analog(duty)

while 1:

    x = radio.receive()
    if x != None:
        if x[0:2] == "as":
            servo(pin8, int(x[2:5]))
            print("Servo = " + str(x[2:5]))
            if int(x[2:5]) > 180:
                print("Out of range")
        elif x[0:2] == "ad":
            print("Display = " + str(x[2:20]))
            display.scroll(x[2:20])
        else:
            pass

