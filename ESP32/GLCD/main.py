'''
Name        : i2c_GLCD.py
Date        : 25/Apr/2023
Brief       : Interface GLCD with ESP32 and display text.
Tested      : OK
Developer   : Rohit Akurdekar
'''

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import freesans20
import writer

# Display dimensions
WIDTH  = 128                                          
HEIGHT = 64                                             

# Display I2C pins
i2c = I2C(sda=Pin(21), scl=Pin(22))
display = SSD1306_I2C(WIDTH, HEIGHT, i2c)

# Draw 
display.fill(0)
display.fill_rect(0, 0, 32, 32, 1)
display.fill_rect(2, 2, 28, 28, 0)
display.vline(9, 8, 22, 1)
display.vline(16, 2, 22, 1)
display.vline(23, 8, 22, 1)
display.fill_rect(26, 24, 2, 4, 1)
# display.text('MicroPython', 40, 0, 1)
display.text('ESP32 with', 40, 12, 1)
# display.text('OLED 128x64', 40, 24, 1)

# Display text with larger font
font_writer = writer.Writer(display, freesans20)
font_writer.set_textpos(5, 40)
font_writer.printstring("MicroPython")

display.show()