from microbit import *
import radio

# Drive F
radio.on()
radio.config(channel=42)
radio.config(power=7)

def servo(pin, degrees):
    degrees = max(0, min(degrees, 180))
    duty = degrees / 180 * 102 + 25
    pin.write_analog(duty)


while 1:
    # BordA----------------------
    x = input("Press Command : ")
    try:
        if x[0] == "a":
            if x[1] == "s":
                if int(x[2:5]) <= 180:
                    print("servo = {}".format(x[2:5]))
                    radio.send(x)
                if int(x[2:5]) > 180:
                radio.send(x)
                    print("Out of range")
            elif x[1] == "d":
                    radio.send(x)
            else:
                pass
    except:
        pass
    # Bord MAIN----------------------

