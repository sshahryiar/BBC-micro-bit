from microbit import *
from utime import sleep_ms
from lcd_display import LCD


lcd = LCD()


lcd.goto(0, 0)
lcd.put_str("Temp./'C:")
lcd.goto(0, 1)
lcd.put_str("Temp./'F:")


while True:
    tc = temperature()
    tf = scale(tc, from_=(0.0, 100.0), to=(32.0, 212.0))
    print("T/'C: " + str("%3u" %tc) + "    T/'F: " + str("%3u" %tf))
    lcd.goto(13, 0)
    lcd.put_str(str("%3u " %tc))
    lcd.goto(13, 1)
    lcd.put_str(str("%3u " %tf))
    sleep_ms(400)
