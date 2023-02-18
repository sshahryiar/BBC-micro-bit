from micropython import const
from microbit import *
from utime import sleep_ms
import random


delay = const(20)


m = 0
n = 0

n1 = Image(
           "00900:"
           "00900:"
           "00900:"
           "00900:"
           "00900")

n2 = Image(
           "99999:"
           "00009:"
           "99999:"
           "90000:"
           "99999")

n3 = Image(
           "99999:"
           "00009:"
           "00999:"
           "00009:"
           "99999")

n4 = Image(
           "90009:"
           "90009:"
           "99999:"
           "00009:"
           "00009")

n5 = Image(
           "99999:"
           "90000:"
           "99999:"
           "00009:"
           "99999")

n6 = Image(
           "99999:"
           "90000:"
           "99999:"
           "90009:"
           "99999")

i1 = Image(
           "00000:"
           "00000:"
           "00900:"
           "00000:"
           "00000")

i2 = Image(
           "00000:"
           "00090:"
           "00000:"
           "09000:"
           "00000")

i3 = Image(
           "00009:"
           "00000:"
           "00900:"
           "00000:"
           "90000")

i4 = Image(
           "00000:"
           "09090:"
           "00000:"
           "09090:"
           "00000")

i5 = Image(
           "90009:"
           "00000:"
           "00900:"
           "00000:"
           "90009")

i6 = Image(
           "90009:"
           "00000:"
           "90009:"
           "00000:"
           "90009")

display.show(" ")

while True:
    gesture = accelerometer.current_gesture()
    print(gesture)
    
    if(button_a.is_pressed() == True):
        m = 1
        
    if(button_b.is_pressed() == True):
        m = 0
    
    if((gesture == "shake") or (gesture == "3g")):
       n = random.randrange(0, 7)
       
    if(n == 1):
       if( m == 0):
           display.show(i1)
       else:
           display.show(n1)
       
    elif(n == 2):
        if( m == 0):
           display.show(i2)
        else:
           display.show(n2)
       
    elif(n == 3):
      if( m == 0):
           display.show(i3)
      else:
           display.show(n3)

    elif(n == 4):
     if( m == 0):
           display.show(i4)
     else:
           display.show(n4)

    elif(n == 5):
     if( m == 0):
           display.show(i5)
     else:
           display.show(n5)
       
    elif(n == 6):
     if( m == 0):
           display.show(i6)
     else:
           display.show(n6)
       
    else:
     display.show(Image.NO)

