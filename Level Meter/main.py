from micropython import const
from microbit import *


N = const(5)
X_min = const(-900)
X_max = const(900)
Y_min = const(-900)
Y_max = const(900)


while(True):
    X = accelerometer.get_x()
    Y = accelerometer.get_y()  
    
    if(X > X_max):
        X = X_max
    elif(X < X_min):
        X = X_min
    
    x = scale(X, from_ = (X_min, X_max), to = (0, (N - 1))) 
      
    if(Y > X_max):
        Y = X_max
    elif(Y < Y_min):
        Y = Y_min
    
    y = scale(Y, from_ = (Y_min, X_max), to = (0, (N - 1)))  
            
    display.clear()   
    display.set_pixel(x, y, 9)

    sleep(100)

