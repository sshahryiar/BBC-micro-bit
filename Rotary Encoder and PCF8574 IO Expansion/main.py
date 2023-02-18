from microbit import *
from machine import *
from PCF8574 import PCF8574
from micropython import const
import time


t_min = const(4000) 
t_max = const(16000)  

max_n = const(7)
min_n = const(0)

m = 0
n = 0
past_n = 0

level_1 = [1, 2, 4, 8, 16, 32, 64, 128]
level_2 = [1, 3, 7, 15, 31, 63, 127, 255]

display.off()

PIN_A = pin2
PIN_B = pin3
PIN_SW = pin4

PIN_A.set_pull( PIN_A.NO_PULL)
PIN_B.set_pull( PIN_B.NO_PULL)
PIN_SW.set_pull( PIN_SW.PULL_UP)

i2c.init(freq = 20000, sda = pin20, scl = pin19)

io = PCF8574(i2c, 0x20)

while(True):
    
    t = time_pulse_us(PIN_A, 1, t_max)
    
    if(PIN_SW.read_digital() == False):
        sleep(300)
        m ^= 1   
    
    if(t >= t_min):
        
        if(PIN_B.read_digital()):
            n -= 1
            if(n <= min_n) :
                n = min_n
        else:
            n += 1
            if(n >= max_n) :
                n = max_n
                
    if(past_n != n):
        past_n = n
    
    if(m == True):
             io.PCF8574_write_byte(level_1[n])
    else:
        io.PCF8574_write_byte(level_2[n])
            
    print(n)
    sleep(40)     