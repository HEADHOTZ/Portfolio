from iled import *
import gc
gc.collect()
f = iled()
while 1:
    for i in range(4):
        f.write_digit(i, 0)
        f.update_display()
        VR = pin2.read_analog() * 1000 /1024
        sleep(VR)
        f.clear()

    for i in range(2):
        f.write_digit(3, i + 1)
        f.update_display()
        VR = pin2.read_analog() * 1000 /1024
        sleep(VR)
        f.clear()

    for i in range(3, -1, -1):
        f.write_digit(i, 3)
        f.update_display()
        VR = pin2.read_analog() * 1000 /1024
        sleep(VR)
        f.clear()

    for i in range(4, 6):
        f.write_digit(0, i)
        f.update_display()
        VR = pin2.read_analog() * 1000 /1024
        sleep(VR)
        f.clear()
