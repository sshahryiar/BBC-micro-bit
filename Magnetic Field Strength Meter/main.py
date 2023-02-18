from microbit import *
from utime import sleep_ms
from lcd_display import LCD


lcd = LCD()

lcd.goto(0, 0)
lcd.put_str("Mag. F. Str./uT:")


while True:
    strength = int(compass.get_field_strength() / 1300.0)
    print(str("%4u" %strength))
    lcd.goto(0, 1)
    lcd.put_str(str("%4u " %strength))
    sleep_ms(400)