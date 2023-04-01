from microbit import*
from utime import sleep_ms


sin_table = [4, 50, 100, 150, 199, 248, 296, 344, 391, 437, 482, 525, 568, 609, 649, 687,
                   723, 758, 790, 821, 850, 877, 902, 924, 945, 963, 978, 992, 1003, 1011, 1018, 1021,
                   1023, 1021, 1018, 1011, 1003, 992, 978, 963, 945, 924, 902, 877, 850, 821, 790, 757,
                   723, 686, 648, 609, 568, 525, 481, 437, 391, 344, 296, 248, 199, 99, 49, 0]


pins = [pin0, pin1, pin2]


for pin in pins:
  pin.set_analog_period_microseconds(1000)
    
while(True):
    for pin in pins:
        for value in sin_table:
            pin.write_analog(value)
            sleep_ms(60)