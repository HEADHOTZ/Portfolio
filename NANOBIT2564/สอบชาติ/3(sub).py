import gc
gc.collect
from microbit import *
from AHT20 import *
from ssd1306 import initialize, clear_oled
from ssd1306_text import add_text
import radio
initialize()
clear_oled()
radio.on()
radio.config(channel = 42)
radio.config(power=7)
i2c.init(freq=100000, sda=pin20, scl=pin19)
addr=0x23
mode = 0
a = AHT20()
def lux():
    i2c.write(addr,bytes([0x10]))
    data = i2c.read(addr, 2)
    lux = (data[0]<<8 | data[1]) / (1.2)
    return lux
def sonar():
    sonar = pin1.read_analog()
    cm = sonar / 10
    return cm
while 1:
    t, h = a.read()
    x = radio.receive()
    if x != None:
        if x[0:1] == 'L':
            display.show('L')
            light = lux()
            msg = ("LUX"+x[1:3] + "=" + "{0:.2f}".format(light))
            add_text(0, 2, "LUX"+x[1:3] + "=" + "{0:.2f}".format(light))
            radio.send(msg)
        elif x[0:1] == 'S':
            display.show('S')
            s = sonar()
            msg = ("Cm" +x[1:3] +"=" + "{0:.2f}".format(s))
            add_text(0, 2, "Cm" +x[1:3] +"=" + "{0:.2f}".format(s))
            radio.send(msg)
        elif x[0:1] == 'H':
            display.show('H')
            msg = ("HU" +x[1:3] +"=" + "{0:.2f}".format(h))
            add_text(0, 2, "HU" +x[1:3] +"=" + "{0:.2f}".format(h))
            radio.send(msg)

