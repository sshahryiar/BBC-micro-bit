from microbit import *
from machine import *
import radio


i = 0
j = 0
k = 0


radio.on()
radio.config(channel=6)

while True:
    if button_a.was_pressed():
        j += 1
        
    if button_b.was_pressed():
        j -= 1
        
    if(j >= 100):
        j = 0
   
    if(j < 0):
        j = 99
   
    if(j != k):
        radio.send(str(j))
    
    k = j
        
    i = radio.receive()
    if(i):
        display.scroll(i)
