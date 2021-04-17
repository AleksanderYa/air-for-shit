from machine import Pin
from time import sleep as sleep


d7 = Pin(13, Pin.OUT)
d5 = Pin(14, Pin.OUT)
d6 = Pin(12, Pin.OUT)

sleep(1)

d7.value(0)
d5.value(0)
d6.value(0)

sleep(5)

d7.value(1)
d5.value(1)
d6.value(1)