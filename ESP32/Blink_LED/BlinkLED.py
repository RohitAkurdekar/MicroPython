from machine import Pin
# import machine
from time import sleep

led = Pin(2, Pin.OUT)
while True:
    led.value(1)
    sleep(1)
    led.value(0)
    sleep(2)