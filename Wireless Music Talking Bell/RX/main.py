from microbit import *
from machine import *
import radio
import music
import speech


radio.config(channel=4)


while True:
    receive = radio.receive()
    
    if(receive == 'A'):
        display.show(Image.MUSIC_QUAVER)
        music.play(music.POWER_UP)
        sleep(100)
        music.play(music.POWER_DOWN)
        sleep(400)
        speech.say("There is someone at the door.", speed=60, pitch=140, throat=135, mouth=125)
        display.clear()