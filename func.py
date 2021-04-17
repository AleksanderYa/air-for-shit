import time, func
from machine import Pin, RTC

#       GPIO PIN
#      ___________
#   16|D0-led   D1|5
#   14|D5       D2|4
#   12|D6       D3|0
#   13|D7   led-D4|2
#   15|D8         |
# best for relay module is GPIO5, GPIO4, GPIO12, GPIO13, GPIO14


# 
fresh_wind = Pin(5, Pin.OUT) # init pin 5, GPIO5
inside_wind =Pin(4, Pin.OUT)


TIME_ON_FRESH_WIND = [0, 0] # [hour, min]
TIME_OFF_FRESH_WIND = [0, 0] # [hour, min]
FRESH_WIND_POS = 0

TIME_ON_INSIDE_WIND = [0, 0] # [hour, min]
TIME_OFF_INSIDE_WIND = [0, 0] # [hour, min]
INSIDE_WIND_POS = 0

def inside():
    if INSIDE_WIND_POS == 1:
        pass
    else:
        pass

