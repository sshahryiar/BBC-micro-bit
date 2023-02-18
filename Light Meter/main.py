from microbit import *
from utime import sleep_ms
from lcd_display import LCD


lcd = LCD()

lcd.goto(0, 0)
lcd.put_str("Light Int./Lux:")


while True:
    strength = (display.read_light_level() * 6)
    print(str("%4u" %strength))
    lcd.goto(0, 1)
    lcd.put_str(str("%4u " %strength))
    sleep_ms(400)
