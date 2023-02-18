from microbit import *
from utime import sleep_ms


sec_LEDs = [[4, 4], [3, 4], [2, 4], [1, 4], [0, 4], [0, 3]]
min_LEDs = [[4, 2], [3, 2], [2, 2], [1, 2], [0, 2], [0, 1]]
hr_LEDs = [[4, 0], [3, 0], [2, 0], [1, 0], [0, 0]]

hr = 10
mn = 10
s = 30
menu = 0


def contrain(value, max_value):
    if(value > max_value):
        return 0
    else:
        return value


def set_value(tmp, value_max):
    if(button_a.is_pressed() == True):
        tmp += 1
        sleep_ms(100)
    tmp = contrain(tmp, value_max)
    return tmp
        

def time_tick():
    global hr, mn, s
    
    s += 1
    if(s > 59):
        s = 0
        mn += 1
    if(mn > 59):
        mn = 0
        hr += 1
    if(hr > 23):
        hr = 0


def display_binary_data(value, num_of_bits, LEDs):
    temp = value
    for i in range(0, num_of_bits):
        bit_value = (temp % 2)
        display.set_pixel(LEDs[i][0], LEDs[i][1], int(bit_value * 9))
        temp = int(temp / 2)
    
    
def display_time():
    global hr, mn, s
    display_binary_data(s, 6, sec_LEDs)
    display_binary_data(mn, 6, min_LEDs)
    display_binary_data(hr, 5, hr_LEDs)
    

def clock():
    global menu
    if(button_a.is_pressed() == True):
        sleep_ms(400)
        if(button_a.is_pressed() == True):
            display.show(Image.ALL_CLOCKS)
            menu = 1
            display.clear()
            while(True):
                set_time()
                if(menu == 4):
                    menu = 0
                    display.show(Image.YES)
                    sleep_ms(2000)
                    display.clear()
                    break 
    else:
        display_time()
        time_tick()
        sleep_ms(1000)
        

def set_time():
    global hr, mn, s, menu
    
    if(button_b.is_pressed() == True):
        sleep_ms(200)
        if(button_b.is_pressed() == True):
            menu += 1
            display.clear()
            sleep_ms(400)
            
    if(menu == 1):
        hr = set_value(hr, 23)
        display_binary_data(hr, 5, hr_LEDs)
    elif(menu == 2):
        mn = set_value(mn, 59)
        display_binary_data(mn, 6, min_LEDs)
    elif(menu == 3):
        s = set_value(s, 59)
        display_binary_data(s, 6, sec_LEDs)


display.clear()


while True:
    clock()
    