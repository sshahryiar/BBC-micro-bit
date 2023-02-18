from micropython import const
from microbit import i2c


Raw_IR_1 = const(0x04)
Raw_IR_1 = const(0x05)
TA = const(0x06)
TOBJ_1 = const(0x07)
TOBJ_2 = const(0x08)


class MLX90614():
    
    def __init__(self, _i2c, addr = 0x5A):
        self.i2c = _i2c
        self.addr = addr
        
        
    def _read_temp(self,reg):
        try:
            self.i2c.write(self.addr, bytes([reg]), repeat = True)
            data = self.i2c.read(self.addr, 3) 
        except OSError as e:
            return None
        value = int(data[1] << 8 | data[0])
        pec = data[2]
        addr_w = (self.addr << 1)
        addr_r = ((self.addr << 1)  |  1)
        byte_seq  =  [addr_w, reg, addr_r, data[0],  data[1]]
        crc8 = MLX90614._crc8( byte_seq, len(byte_seq))
        if(crc8 == pec):
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
        polynomial = 0x07 # P(x)=x^8+x^2+x^1+1 = 100000111
        crc = 0x00 
        for i in range(n):
            crc ^= data[i]
            for j in range(0, 8):
                if(crc & 0x80):
                    crc = ((crc << 1) ^ polynomial)
                else:
                    crc <<= 1
        return (crc & 0xFF)
