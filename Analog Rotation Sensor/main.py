from microbit import *
from machine import *
from utime import sleep_us


adc_pin = pin0


def adc_avg():
    i = 64
    v = 0
    r = 0
    avg = 0
    
    while(i > 0):
        avg += adc_pin.read_analog()
        i -= 1
        sleep_us(10)
        
    avg >>= 6
    rot = ((avg * 360.0) / 1024)
    
    return rot


while(True):
    rot = adc_avg()
    if((rot>= 22.5) and (rot< 67.5)):
        display.show(Image.ARROW_NE)
    elif((rot>= 67.5) and (rot< 112.5)):
        display.show(Image.ARROW_E)
    elif((rot>= 112.5) and (rot< 157.5)):
        display.show(Image.ARROW_SE)
    elif((rot>= 157.5) and (rot< 202.5)):
        display.show(Image.ARROW_S)
    elif((rot>= 202.5) and (rot< 247.5)):
        display.show(Image.ARROW_SW)
    elif((rot>= 247.5) and (rot< 292.5)):
        display.show(Image.ARROW_W)
    elif((rot>= 292.5) and (rot< 337.5)):
        display.show(Image.ARROW_NW)
    else: 
        display.show(Image.ARROW_N)
