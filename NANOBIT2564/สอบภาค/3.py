import gc
gc.collect()
from microbit import *
from AHT20 import *
from iled4 import *
import music
mode = 0
st_sw = 0
ch = ["t","T","H","U","L"]
enter = pin14
esc = pin12
a = AHT20()
f = iled4()
i2c.init(freq=100000, sda=pin20, scl=pin19)
addr=0x23

def lux():
    i2c.write(addr,bytes([0x10]))
    data = i2c.read(addr, 2)
    lux = (data[0]<<8 | data[1]) / (1.2)
    return lux

while 1:
    light = lux()
    sonar = pin1.read_analog()
    cm = sonar / 10
    temp = temperature()
    t,h = a.read()
    mode = int((pin2.read_analog()*4/1023)+1)
    if not esc.read_digital():
        while not esc.read_digital():
            sleep(10)
        music.pitch(2000,100)
        st_sw = 0
    elif not enter.read_digital():
        while not enter.read_digital():
            sleep(10)
        music.pitch(2000,100)
        st_sw = 1
    else:
        pass
    if st_sw == 0:
        display.show(ch[mode-1])
        f.clear()
    elif st_sw == 1:
        if mode == 1:
            print(temp)
            f.print(temp)
            f.update_display()
        elif mode == 2:
            x = int(t*100)
            print(t)
            f.print(x)
            f.set_decimal(1)
            f.update_display()
        elif mode == 3:
            x = int(h*100)
            print(h)
            f.print(x)
            f.set_decimal(1)
            f.update_display()
        elif mode == 4:
            x = int(cm*10)
            print(cm)
            f.print(x)
            f.set_decimal(2)
            f.update_display()
        elif mode == 5:
            print(int(light))
            f.print(int(light))
            f.update_display()
