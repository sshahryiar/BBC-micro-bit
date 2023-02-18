from microbit import *
from utime import sleep_ms
from micropython import const


ON_Threshold_min = const(25)
ON_Threshold_max = const(35)

OFF_Threshold_min = const(50)
OFF_Threshold_max = const(75)

check_counter = const(10)


lights_on = True
time_counter = 0
image = Image(5, 5, bytearray([9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]))


while True:
    light_level = display.read_light_level()
    print(light_level)
    
    if(lights_on == True): 
        if((light_level > OFF_Threshold_min) and (time_counter < check_counter)):
            time_counter += 1
            sleep_ms(300)
            
        if((light_level > OFF_Threshold_max) and (time_counter >= check_counter)):
            lights_on = False
            time_counter = 0
            
        if(light_level < OFF_Threshold_max):
            time_counter = 0
        
        display.show(image)
        sleep_ms(60)
        display.clear()
        sleep_ms(600)
        
    else: 
        if((light_level < ON_Threshold_max) and (time_counter < check_counter)):
            time_counter += 1
            sleep_ms(300)
        
        if((light_level < ON_Threshold_min) and (time_counter >= check_counter)):
            lights_on = True
            time_counter = 0
            display.clear()
            
        if(light_level > ON_Threshold_max):
            time_counter = 0

