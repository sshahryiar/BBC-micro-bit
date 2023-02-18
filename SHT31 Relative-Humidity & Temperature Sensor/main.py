from microbit import *
from utime import sleep_ms
from I2C_LCD import *
from SHT3x import *


i2c.init(freq = 20000, sda = pin20, scl = pin19)

lcd = I2C_LCD(i2c, 0x27)
sht3x = SHT3x(i2c, 0x44)
sht3x.reset()


lcd.goto_xy(0, 0)
lcd.put_str("Tmp/'C:")
lcd.goto_xy(0, 1)
lcd.put_str("R.H./%:")


while(True):
    sht3x.measure()
    t, rh = sht3x.read()
    lcd.goto_xy(12, 0)
    lcd.put_str(str("%2.1f " %t))
    lcd.goto_xy(12, 1)
    lcd.put_str(str("%2.1f " %rh))
    sleep_ms(200)