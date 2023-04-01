from microbit import *
from micropython import const
from utime import sleep_ms


SDS011_MESSAGE_LENGTH = const(10)

SDS011_MESSAGE_HEADER = const(0xAA)
SDS011_COMMANDER_NO = const(0xC0)
SDS011_MESSAGE_TRAILER = const(0xAB)

SDS011_MESSAGE_HEADER_BYTE_ID = const(0x00)
SDS011_COMMANDER_NO_BYTE_ID = const(0x01)
SDS011_PM25_LB_BYTE_ID = const(0x02)
SDS011_PM25_HB_BYTE_ID = const(0x03)
SDS011_PM10_LB_BYTE_ID = const(0x04)
SDS011_PM10_HB_BYTE_ID = const(0x05)
SDS011_ID1_BYTE_ID = const(0x06)
SDS011_ID2_BYTE_ID = const(0x07)
SDS011_CRC_BYTE_ID = const(0x08)
SDS011_MESSAGE_TRAILER_BYTE_ID = const(0x09)


class SDS011():
    
    def __init__(self, _uart):
        self.uart = _uart
        
        
    def read(self):
        crc = 0
        pm10 = 0
        pm25 = 0
        
        try:
            data = uart.read(SDS011_MESSAGE_LENGTH)
        except:
            print("Error Reading Sensor!")
        sleep_ms(1000)
        
        if((data[SDS011_MESSAGE_HEADER_BYTE_ID] == SDS011_MESSAGE_HEADER) and (data[SDS011_COMMANDER_NO_BYTE_ID] == SDS011_COMMANDER_NO)):
            for i in range(SDS011_PM25_LB_BYTE_ID, SDS011_CRC_BYTE_ID):
                crc += data[i]
                
            crc &= 0xFF

            if((data[SDS011_CRC_BYTE_ID] == crc) and (data[SDS011_MESSAGE_TRAILER_BYTE_ID] == SDS011_MESSAGE_TRAILER)):
                pm25 = (((data[SDS011_PM25_HB_BYTE_ID] << 0x08) + data[SDS011_PM25_LB_BYTE_ID]) / 10.0)
                pm10 = (((data[SDS011_PM10_HB_BYTE_ID] << 0x08) + data[SDS011_PM10_LB_BYTE_ID]) / 10.0)
                return (pm25, pm10, data[SDS011_ID1_BYTE_ID], data[SDS011_ID2_BYTE_ID])
            
            else:
                return (-1, -1, -1, -1)
            
        else:
                return (0, 0, 0, 0)
