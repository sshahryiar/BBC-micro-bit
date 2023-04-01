from microbit import *
from utime import sleep_ms
from SONAR_sensor import *
from neopixel import NeoPixel


hc = SONAR_sensor()
np = NeoPixel(pin0, 8)


def clear_neopixel():
    for i in range (-1, 8):
        np[i] = (0, 0, 0)
        np.show()


while(True):
    r = hc.get_range()
    print("Range: " + str("%4u" %r) + " mm")
    
    if((r > 0) and (r < 100)):
        clear_neopixel()
        np[0] = (200, 0, 0)
    
    elif((r >= 100) and (r < 200)):
        clear_neopixel()
        np[0] = (200, 0, 0)
        np[1] = (200, 0, 0)
        
    elif((r >= 200) and (r < 300)):
        clear_neopixel()
        np[0] = (200, 0, 0)
        np[1] = (200, 0, 0)
        np[2] = (200, 0, 0)
        
    elif((r >= 300) and (r < 400)):
        clear_neopixel()
        np[0] = (200, 0, 0)
        np[1] = (200, 0, 0)
        np[2] = (200, 0, 0)
        np[3] = (128, 128, 0)
        
    elif((r >= 400) and (r < 500)):
        clear_neopixel()
        np[0] = (200, 0, 0)
        np[1] = (200, 0, 0)
        np[2] = (200, 0, 0)
        np[3] = (128, 128, 0)
        np[4] = (128, 128, 0)
        
    elif((r >= 500) and (r < 600)):
        clear_neopixel()
        np[0] = (200, 0, 0)
        np[1] = (200, 0, 0)
        np[2] = (200, 0, 0)
        np[3] = (128, 128, 0)
        np[4] = (128, 128, 0)
        np[5] = (0, 200, 0)
    
    elif((r >= 600) and (r < 700)):
        clear_neopixel()
        np[0] = (200, 0, 0)
        np[1] = (200, 0, 0)
        np[2] = (200, 0, 0)
        np[3] = (128, 128, 0)
        np[4] = (128, 128, 0)
        np[5] = (0, 200, 0)
        np[6] = (0, 200, 0)
        
    elif(r >= 800):
        clear_neopixel()
        np[0] = (200, 0, 0)
        np[1] = (200, 0, 0)
        np[2] = (200, 0, 0)
        np[3] = (128, 128, 0)
        np[4] = (128, 128, 0)
        np[5] = (0, 200, 0)
        np[6] = (0, 200, 0)
        np[7] = (0, 200, 0)

    else:
        clear_neopixel()

    np.show()
    sleep_ms(260)

