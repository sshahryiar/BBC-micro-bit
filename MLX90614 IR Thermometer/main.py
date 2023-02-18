from microbit import *
from utime import sleep_ms
from I2C_LCD import *
from MLX90614 import *


i2c.init(freq = 20000, sda = pin20, scl = pin19)

mlx = MLX90614(i2c)
lcd = I2C_LCD(i2c, 0x27)


lcd.goto_xy(0, 0)
lcd.put_str("T.amb./'C:")
lcd.goto_xy(0, 1)
lcd.put_str("T.obj./'C:")


while True:
    ta = mlx.read_Ta()
    tobj1 = mlx.read_Tobj1()
    if((ta != None) and (tobj1 != None)):
        lcd.goto_xy(11, 0)
        lcd.put_str(str("%3.1f " %ta))
        lcd.goto_xy(11, 1)
        lcd.put_str(str("%3.1f " %tobj1))
        sleep_ms(200)
