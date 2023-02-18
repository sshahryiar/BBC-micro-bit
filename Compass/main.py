from microbit import *
from utime import sleep_ms

heading = 0

display.show(Image.ALL_CLOCKS)
display.scroll("micro:Bit Compass", delay = 180)
sleep_ms(1000)
display.clear()

while(True):
    heading = compass.heading()
           
    if((heading >= 22.5) and (heading < 67.5)):
        display.show(Image.ARROW_NE)
    elif((heading >= 67.5) and (heading < 112.5)):
        display.show(Image.ARROW_E)
    elif((heading >= 112.5) and (heading < 157.5)):
        display.show(Image.ARROW_SE)
    elif((heading >= 157.5) and (heading < 202.5)):
        display.show(Image.ARROW_S)
    elif((heading >= 202.5) and (heading < 247.5)):
        display.show(Image.ARROW_SW)
    elif((heading >= 247.5) and (heading < 292.5)):
        display.show(Image.ARROW_W)
    elif((heading >= 292.5) and (heading < 337.5)):
        display.show(Image.ARROW_NW)
    else: 
        display.show(Image.ARROW_N)
    
    print("Heading: " + str("%3.1f" %heading) + "°N")
    sleep_ms(200)
    
    if(button_a.is_pressed()):
        sleep_ms(200)
        if(button_a.is_pressed()):
            print("\r\n")
            print("Calibration Mode.")
            print("Follow on screen instructions.")
            print("\r\n")
            display.show(Image.ALL_ARROWS)
            compass.clear_calibration()
            compass.calibrate()
            sleep_ms(1200)
        display.clear()
