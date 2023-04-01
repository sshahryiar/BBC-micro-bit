from microbit import *
from utime import sleep_ms
from I2C_LCD import *
from SDS011 import *


i2c.init(freq = 20000, sda = pin20, scl = pin19)
uart.init(baudrate=9600, bits=8, parity=None, stop=1, tx=pin0, rx=pin1)

lcd = I2C_LCD(i2c, 0x27)
sds = SDS011(uart)

lcd.goto_xy(0, 0)
lcd.put_str("PM2.5")
lcd.goto_xy(0, 1)
lcd.put_str("PM10")

lcd.goto_xy(11, 0)
lcd.put_str("ug/m3")
lcd.goto_xy(11, 1)
lcd.put_str("ug/m3")


while(True):
    pm25, pm10, id1, id2 = sds.read()
    lcd.goto_xy(6, 0)
    lcd.put_str(str("%3.1f" %pm25))
    lcd.goto_xy(6, 1)
    lcd.put_str(str("%3.1f" %pm10))
