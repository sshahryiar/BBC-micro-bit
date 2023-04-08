from microbit import *
from machine import *
import radio


radio.config(channel=4)


while True:
    if button_a.was_pressed():
        display.show(Image.MUSIC_QUAVERS)
        sleep(40)
        radio.on()
        sleep(200)
        radio.send('A')
        radio.off()
        sleep(1000)
        display.clear()