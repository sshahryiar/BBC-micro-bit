from microbit import *
from utime import sleep_ms
from MLX90614 import *


mlx = MLX90614()


while(True):
    ta = mlx.read_Ta()
    tobj1 = mlx.read_Tobj1()
    if((ta != None) and (tobj1 != None)):
        display.scroll(("Ta: " + str("%3.1f" %ta)), 160)
        display.scroll(("To: " + str("%3.1f" %tobj1)), 160)
        sleep_ms(200)