from microbit import *
from machine import *
from utime import sleep_us


TMP36_pin = pin1


def read_TMP36():
    i = 16
    v = 0
    t = 0
    avg = 0
    
    while(i > 0):
        avg += TMP36_pin.read_analog()
        i -= 1
        sleep_us(10)
        
    avg >>= 4
    
    v =  ((avg * 3300.0) / 1023.0)
    t =  ((v - 500.0) / 10.0)
    
    return t


while(True):
    temp = read_TMP36()
    display.scroll(str("%2.1f'C" %temp))
