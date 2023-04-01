from machine import *
from microbit import *
from micropython import const
from utime import sleep_us, ticks_us


TIMEOUT_US = const(38000)


class SONAR_sensor():
    
    def __init__(self, echo_pin = pin11, trigger_pin = pin12, trigger_time_us = 20, timeout = TIMEOUT_US, scaling_factor = 5.8):
       self.trigger_pin = trigger_pin
       self.echo_pin = echo_pin
       self.trigger_time = trigger_time_us
       self.timeout = timeout
       self.scaling_factor = scaling_factor
       display.off()
       self.trigger_pin.write_digital(0)
        
        
    def get_range(self):
        d = 0
        t1 = 0
        t2 = 0
        cnt = 0
        
        self.trigger_pin.write_digital(1)
        sleep_us(self.trigger_time)
        self.trigger_pin.write_digital(0)
        
        cnt = self.timeout
        while((cnt > 0) and (self.echo_pin.read_digital() == False)):
            cnt += 1
            sleep_us(1)
        
        t1 = ticks_us()
        
        cnt = self.timeout
        while((cnt > 0) and (self.echo_pin.read_digital() == True)):
            cnt += 1
            sleep_us(1)
        
        t2 = ticks_us()
        
        d = (t2 - t1)
        
        if(d < 0):
            d  = 0
            
        d = int(d / self.scaling_factor)
        
        return d
