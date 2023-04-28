from machine import Pin
# import machine
from time import sleep

LED_PIN = 2

led = Pin(LED_PIN, Pin.OUT)
while True:
    print("Hi")
    led.value(1)
    sleep(1)
    led.value(0)
    sleep(2)