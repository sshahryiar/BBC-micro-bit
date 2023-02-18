import microbit
from microbit import *
from micropython import const


clear_display        = const(0x01)
goto_home            = const(0x02)
         
cursor_direction_inc = const(0x06)
cursor_direction_dec = const(0x04)
display_shift        = const(0x05)
display_no_shift     = const(0x04)

display_on           = const(0x0C)
display_off          = const(0x0A)
cursor_on            = const(0x0A)
cursor_off           = const(0x08)
blink_on             = const(0x09)
blink_off            = const(0x08)
                                    
_8_pin_interface     = const(0x30)
_4_pin_interface     = const(0x20)
_2_row_display       = const(0x28)
_1_row_display       = const(0x20)
_5x10_dots           = const(0x60)
_5x7_dots            = const(0x20)

line_1_y_pos         = const(0x00)
line_2_y_pos         = const(0x40)
line_3_y_pos         = const(0x14)
line_4_y_pos         = const(0x54)


SCK_PIN = pin13
MOSI_PIN = pin15
CS_PIN = pin16


spi_buf = bytearray(1)


class LCD():
        
    def __init__(self):
        self.data_value = 0x00
        CS_PIN.write_digital(1)
        spi.init(baudrate = 4000000, bits = 8, mode = 0, sclk = SCK_PIN, mosi = MOSI_PIN, miso = None)
        self.init()
        
    
    def init(self):
        self.data_value = 0x08
        self.SIPO()
       
        self.init_seq(0x30)
        self.init_seq(0x30)
        self.init_seq(0x20)
        
        self.command((_4_pin_interface | _2_row_display | _5x7_dots))         
        self.command((display_on | cursor_off | blink_off))
        self.command(clear_display)         
        self.command((cursor_direction_inc | display_no_shift))
        
        
    def SIPO(self):
        global spi_buf
        spi_buf[0] = self.data_value
        CS_PIN.write_digital(0)
        spi.write(spi_buf)
        CS_PIN.write_digital(1)    
    
    
    def command(self, value):
        self.data_value &= 0xFB
        self.SIPO()
        self.send_nibbles(value)
        
        
    def send_data(self, value):
        self.data_value |= 0x04
        self.SIPO()
        self.send_nibbles(value)
        
    
    def send_nibbles(self, lcd_data):
        temp = (lcd_data & 0xF0)
        self.data_value &= 0x0F
        self.data_value |= temp
        self.SIPO()
        self.data_value |= 0x08
        self.SIPO()
        self.data_value &= 0xF7
        self.SIPO()

        temp = (lcd_data & 0x0F)
        temp <<= 0x04
        self.data_value &= 0x0F
        self.data_value |= temp
        self.SIPO()     
        self.data_value |= 0x08
        self.SIPO()
        self.data_value &= 0xF7
        self.SIPO()
        
    
    def init_seq(self, value):
        self.data_value = value
        self.SIPO()
        self.data_value |= 0x08
        self.SIPO()
        self.data_value &= 0xF7
        self.SIPO()
    
    
    def toggle_en(self):
        self.data_value |= 0x08
        self.SIPO()
        self.data_value &= 0xF7
        self.SIPO()
    
        
    def clear_home(self):
        self.command(clear_display)
        self.command(goto_home)
        
        
    def goto(self, x_pos, y_pos):
        if(y_pos == 0):
            self.command(0x80 | x_pos)
        else:
            self.command(0x80 | 0x40 | x_pos)
            
            
    def put_chr(self, ch):        
        self.send_data(ord(ch))
        
            
    def put_str(self, ch_string):        
        for chr in ch_string:
            self.put_chr(chr)
    