class PCF8574():
    
    def __init__(self, _i2c, _i2c_addr):        
        self.i2c = _i2c
        self.i2c_addr = _i2c_addr


    def PCF8574_write_byte(self, value):        
        self.i2c.write(self.i2c_addr, bytes([value]))
        
        
    def PCF8574_read_byte(self, mask):        
        self.PCF8574_write_byte(mask)
        retval = self.i2c.read(self.i2c_addr, 1)        
        return retval[0]
