from micropython import const
from microbit import *


SDA_pin = pin20
SCL_pin = pin19


Raw_IR_1 = const(0x04)
Raw_IR_1 = const(0x05)
TA = const(0x06)
TOBJ_1 = const(0x07)
TOBJ_2 = const(0x08)


class MLX90614:
    def __init__(self, addr = 0x5a):
        self.addr = addr
        i2c.init(freq = 100000, sda = SDA_pin, scl = SCL_pin)
        
    def _read_temp(self,reg):
        try:
            i2c.write(self.addr, bytes([reg]), repeat = True)
            data = i2c.read(self.addr, 3) 
        except OSError as e:
            return None
        value = int(data[1] << 8 | data[0])
        pec = data[2]
        addr_w = (self.addr << 1)
        addr_r = (self.addr << 1) | 1
        byte_seq  =  [addr_w, reg, addr_r, data[0],  data[1]]
        crc8 = MLX90614._crc8( byte_seq, len(byte_seq))
        if crc8 == pec:
            return ((value * 0.02) - 273.15) 
        else: 
            return None
         
         
    def read_Ta(self): 
        return self._read_temp(TA)
    
    
    def read_Tobj1(self): 
        return self._read_temp(TOBJ_1)
    
    
    def read_Tobj2(self): 
        return self._read_temp(TOBJ_2)
        
        
    def _crc8(data, n):
        POLYNOMIAL = 0x07 # P(x)=x^8+x^2+x^1+1 = 100000111
        crc = 0x00 
        for i in range(n):
            crc ^= data[i]
            for j in range(0, 8):
                if crc & 0x80:
                    crc = ((crc << 1) ^ POLYNOMIAL)
                else:
                    crc = (crc << 1)
        return (crc & 0xff)
