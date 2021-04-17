import time
from machine import Pin, RTC

#       GPIO PIN
#      ___________
#   16|D0-led   D1|5
#   14|D5       D2|4
#   12|D6       D3|0
#   13|D7   led-D4|2
#   15|D8         |
# best for relay module is GPIO5, GPIO4, GPIO12, GPIO13, GPIO14

rtc = RTC() #  init module realtime
hour = rtc.datetime()[4] + 2   # hours,  Kiev +2
mint = rtc.datetime()[5] # minut

TIME_ON_FRESH_WIND = [0, 0] # [hour, min]
FRESH_WIND_POS = 1 # OFF pin
print(TIME_ON_FRESH_WIND)

TIME_ON_INSIDE_WIND = [0, 0] # [hour, min]
INSIDE_WIND_POS = 1 # OFF pin
#

fresh_wind = Pin(16, Pin.OUT) # init pin 5, GPIO5
fresh_wind.on() # off pin
inside_wind =Pin(2, Pin.OUT) # init pin 4, GPIO4
inside_wind.on() # off pin


if len(str(rtc.datetime()[5])) == 1:
    print('{0}:0{1}'.format(hour, mint)) # print to format 00:00
else:
    print('{0}:{1}'.format(hour, mint)) # print to format 00:00



def inside_wind_on_off(tmr_pause=1, tmr_work=1):
    mit= rtc.datetime()[5]
    hou= rtc.datetime()[4] + 2
    global INSIDE_WIND_POS, TIME_ON_INSIDE_WIND 
    if INSIDE_WIND_POS == 1:
        print(mit, TIME_ON_INSIDE_WIND[1])
#        print(TIME_ON_INSIDE_WIND[1])
        if mit >= TIME_ON_INSIDE_WIND[1] or TIME_ON_INSIDE_WIND[0] < hou:
            inside_wind.off() # to ON
            INSIDE_WIND_POS = 0
            TIME_ON_INSIDE_WIND = time_shit([hou, mit], tmr_work)
            print(TIME_ON_INSIDE_WIND)
    elif INSIDE_WIND_POS == 0:
        print(mit, TIME_ON_INSIDE_WIND[1])
        if mit >= TIME_ON_INSIDE_WIND[1] or TIME_ON_INSIDE_WIND[0] < hou:
            inside_wind.on() # to OFF
            INSIDE_WIND_POS = 1
            TIME_ON_INSIDE_WIND = time_shit([hou, mit], tmr_pause)
            print(TIME_ON_INSIDE_WIND)


def fresh_wind_on_off(tmr_pause=1, tmr_work=1):
    mit = rtc.datetime()[5]
    hou = rtc.datetime()[4] + 2
    global FRESH_WIND_POS, TIME_ON_FRESH_WIND  
    if FRESH_WIND_POS == 1:
        print(mit, TIME_ON_FRESH_WIND[1])
#        print(TIME_ON_INSIDE_WIND[1])
        if mit >= TIME_ON_FRESH_WIND[1] or TIME_ON_FRESH_WIND[0] < hou:
            fresh_wind.off() # to ON
            FRESH_WIND_POS = 0
            TIME_ON_FRESH_WIND = time_shit([hou, mit], tmr_work)
            print(TIME_ON_FRESH_WIND)
    elif FRESH_WIND_POS == 0:
        print(mit, TIME_ON_FRESH_WIND[1])
        if mit >= TIME_ON_FRESH_WIND[1] or TIME_ON_FRESH_WIND[0] < hou:
            fresh_wind.on() # to OFF
            FRESH_WIND_POS = 1
            TIME_ON_FRESH_WIND = time_shit([hou, mit], tmr_pause)
            print(TIME_ON_FRESH_WIND)

        
        
def time_shit(tm, timer):
    h = tm[0]
    m = tm[1]
    m = m + timer
    if m > 59:
        m = m - 60
        if h == 24:
            h -= 23
        else:
            h += 1
    return [h, m]
        
for i in range(1000):
    inside_wind_on_off()
    time.sleep(2)
    fresh_wind_on_off()
    time.sleep(2)