# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
#import webrepl
#webrepl.start()
gc.collect()
#       GPIO PIN
#      ___________
#   16|D0-led   D1|5
#   14|D5       D2|4
#   12|D6       D3|0
#   13|D7   led-D4|2
#   15|D8         |
# best for relay module is GPIO5, GPIO4, GPIO12, GPIO13, GPIO14
#import test


