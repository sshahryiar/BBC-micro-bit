from microbit import *
from utime import sleep_ms
from SONAR_sensor import *
from MAX72xx import *


r = 0

hc = SONAR_sensor()
disp = MAX72xx()


while(True):
    r = hc.get_range()
    print("Range: " + str("%4u" %r) + " mm")
    disp.write(1, (r % 10))
    disp.write(2, ((r // 10) % 10))
    disp.write(3, ((r // 100) % 10))
    disp.write(4, ((r // 1000) % 10))
    sleep_ms(200)
