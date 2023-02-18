from microbit import *
from SHT3x import *


i2c.init(freq = 20000, sda = pin20, scl = pin19)


sht3x = SHT3x(i2c, 0x44)
sht3x.reset()


while(True):
    sht3x.measure()
    t, rh = sht3x.read()
    display.scroll("T/'C:" + str("%2.1f" %t) + "   RH/%:" + str("%2.1f" %rh))
    sleep(1000)
