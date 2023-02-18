from micropython import const
from utime import sleep_ms

         
power_down = const(0x00)
power_up	= const(0x01)
reset = const(0x07)
cont_H_res_mode1 = const(0x10)
cont_H_res_mode2 = const(0x11)
cont_L_res_mode = const(0x13)                                          
one_time_H_res_mode1 = const(0x20)
one_time_H_res_mode2 = const(0x21)
one_time_L_res_mode = const(0x23)


class BH1750():
    
    def __init__(self, _i2c, _i2c_addr = 0x23):
        
        self.i2c = _i2c
        self.i2c_addr = _i2c_addr
        self.i2c.write(self.i2c_addr, bytes([power_down]))
        sleep_ms(100)
        self.init()
        
    
    def init(self):
        self.i2c.write(self.i2c_addr, bytearray([power_up]) )
        self.i2c.write(self.i2c_addr, bytearray([reset]) )
        sleep_ms(200)
        self.i2c.write(self.i2c_addr, bytearray([cont_H_res_mode1]) )
        sleep_ms(150)
        
        
    def read(self):
        value  = self.i2c.read(self.i2c_addr, 2) 
        lux = ((value[0x00] << 0x08 | value[0x01]) / 1.2)
        return lux
