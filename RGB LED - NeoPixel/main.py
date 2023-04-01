from microbit import*
from utime import sleep_ms
from neopixel import NeoPixel


sin_table_1 = [0, 24, 49, 74, 97, 120, 141, 161, 180, 197, 212, 224, 235, 244, 250, 253,
                    255, 253, 250, 244, 235, 224, 211, 197, 180, 161, 141, 120, 97, 73, 49, 24]

sin_table_2 = [212, 224, 235, 244, 250, 253, 255, 253, 250, 244, 235, 224, 211, 197,
                       180, 161, 141, 120, 97, 73, 49, 24, 0, 24, 49, 74, 97, 120, 141, 161, 180, 197]

sin_table_3 = [235, 224, 211, 197, 180, 161, 141, 120, 97, 73, 49, 24, 0, 24, 49, 74, 97,
                       120, 141, 161, 180, 197, 212, 224, 235, 244, 250, 253, 255, 253, 250, 244]


np = NeoPixel(pin1, 2)

    
while(True):
    for i in range (0, 32):
        np[0] = (sin_table_1[i], sin_table_2[i], sin_table_3[i])
        np[1] = (sin_table_3[i], sin_table_2[i], sin_table_1[i])
        np.show()        
        sleep_ms(90)
