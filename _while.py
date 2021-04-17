from machine import Pin, RTC
import time

rtc = RTC()

#def test():
#    res = Pin(2, Pin.OUT).value(0)
#    time.sleep(3)
#    res2 = Pin(2, Pin.OUT).value(1)
#    return res, time.sleep(3), res2
    
def on_off(pin, val=0):
    Pin(pin, Pin.OUT).value(val)
    
def rep(col):
    for i in range(col):
        Pin(2, Pin.OUT).value(0)
        time.sleep(0.5)
        Pin(2, Pin.OUT).value(1)
        time.sleep(0.5)
        print(i)
        
hour = rtc.datetime()[4] + 2
mint = rtc.datetime()[5]



while True:
    if hour > 23 or hour < 7:
#        on_off(2, 1)
#        time.sleep(2)
        print(hour)
        rep(hour)
        print('All good')
        break
    elif hour < 23 or hour > 7:
#        on_off(2)
#         time.sleep(2)
        print(hour)
        rep(hour)
        print('All good')
        break
#    elif PIN:
#        name = False