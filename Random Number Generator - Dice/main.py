from microbit import *
import random
    

while True:        
    if((button_a.is_pressed()) or (button_b.is_pressed())):
        seed = pin0.read_analog()
        random.seed(seed)
    
        if(button_a.was_pressed()):
            display.show(random.randint(1, 6))
        
        if(button_b.was_pressed()):
            display.clear()