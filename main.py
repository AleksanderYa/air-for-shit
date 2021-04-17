from machine import Pin, RTC
import time

rtc = RTC()

hour = rtc.datetime()[4]
mint = rtc.datetime()[5]

tm = str(hour + 2) + ':' + str(mint)
print(tm)


#       GPIO PIN
#      ___________
#   16|D0-led   D1|5
#   14|D5       D2|4
#   12|D6       D3|0
#   13|D7   led-D4|2
#   15|D8         |
# best for relay module is GPIO5, GPIO4, GPIO12, GPIO13, GPIO14