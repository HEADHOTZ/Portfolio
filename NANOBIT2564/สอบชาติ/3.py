from microbit import *
import radio
radio.on()
radio.config(channel = 40)
radio.config(power=7)
while 1:
    if button_a.is_pressed():
        while button_a.is_pressed():
            sleep(10)
        msg = "L"
        radio.send(msg)
