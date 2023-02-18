from microbit import *
from utime import sleep_ms
from I2C_LCD import *
from BH1750 import *


i2c.init(freq = 20000, sda = pin20, scl = pin19)


lcd = I2C_LCD(i2c, 0x27)
light = BH1750(i2c, 0x23)


lcd.goto_xy(0, 0)
lcd.put_str("Micro:Bit BH1750")
lcd.goto_xy(0, 1)
lcd.put_str("Lux/lx:")


while(True):
    lux = light.read()
    lcd.goto_xy(12, 1)
    lcd.put_str(str("%4.0f " %lux))
    sleep_ms(200)