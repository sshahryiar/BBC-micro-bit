from micropython import const


polynomial = const(0x31)


class SHT3x:
    def __init__(self, _i2c, _addr):
        self.i2c  = _i2c
        self.addr = _addr
    
    
    def reset(self):
        self.i2c.write(self.addr, bytearray([0x30, 0xA2]))


    def measure(self):
        self.i2c.write(self.addr, bytearray([0x2C, 0x06]))
 
 
    def read(self):
        raw_data = self.i2c.read(self.addr,  6)

        if (self.crc8(raw_data[0:2]) != raw_data[2]) or (self.crc8(raw_data[3:5]) != raw_data[5]):
            raise RuntimeError('SHT3x: CRC mismatch!')
        
        t = (-45 + (175 * ((raw_data[0] << 8) + raw_data[1])  / 65535.0))
        rh = (100 * ((raw_data[3] << 8) + raw_data[4]) / 65535.0)
        return (t, rh)


    def crc8(self, buf):
        crc = 0xff;
        for i in range(0, len(buf)):
            crc ^= buf[i]
            for j in range(8):
                if crc & 0x80:
                    crc = ((crc << 1) ^ polynomial)
                else:
                    crc = (crc << 1)
        return (crc & 0xff)
