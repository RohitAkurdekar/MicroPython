from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
import utime
import freesans20
import writer


WIDTH  = 128                                          
HEIGHT = 64                                             

i2c = I2C(sda=Pin(21), scl=Pin(22))
display = SSD1306_I2C(WIDTH, HEIGHT, i2c)

while True:

    display.fill(0)
    display.fill_rect(0, 0, 32, 32, 1)
    display.fill_rect(2, 2, 28, 28, 0)
    display.vline(9, 8, 22, 1)
    display.vline(16, 2, 22, 1)
    display.vline(23, 8, 22, 1)
    display.fill_rect(26, 24, 2, 4, 1)
    # display.text('MicroPython', 40, 0, 1)
    # display.text('SSD1306', 40, 12, 1)
    # display.text('OLED 128x64', 40, 24, 1)

    font_writer = writer.Writer(display, freesans20)
    font_writer.set_textpos(5, 115)
    font_writer.printstring("MicroPython")

    display.show()

# oled.fill(0)
# oled.fill_rect(0, 0, 32, 32, 1)
# oled.fill_rect(2, 2, 28, 28, 0)
# oled.vline(9, 8, 22, 1)
# oled.vline(16, 2, 22, 1)
# oled.vline(23, 8, 22, 1)
# oled.fill_rect(26, 24, 2, 4, 1)

# # oled.text('MicroPython', 40, 0, 1)
# # oled.text('SSD1306', 40, 12, 1)
# # oled.text('OLED 128x64', 40, 24, 1)
# oled.show()