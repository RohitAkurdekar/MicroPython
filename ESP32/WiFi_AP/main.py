# boot menu
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

from machine import Pin

SSID = 'MicroPython-AP1'
PASSWORD = '123456789'

try:
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid=SSID, password=PASSWORD)
except:
    pass

while ap.active() == False:
    pass

led = Pin(2, Pin.OUT)
led.value(1)
print('Connection successful')
print(ap.ifconfig())

while True:
    print("")
