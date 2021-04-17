from machine import Pin
#       GPIO PIN
#      ___________
#   16|D0-led   D1|5
#   14|D5       D2|4
#   12|D6       D3|0
#   13|D7   led-D4|2
#   15|D8         |
# best for relay module is GPIO5, GPIO4, GPIO12, GPIO13, GPIO14
def callback_in(p):
    Pin(2, Pin.OUT).value(0)
    print('pin change', p)


def callback_out(p):
    Pin(2, Pin.OUT).value(1)
    print('pin change', p)
    
    
p0 = Pin(0, Pin.IN)
p2 = Pin(15, Pin.IN)
#Pin(4, Pin.OUT).value(1)

p0.irq(trigger=Pin.IRQ_FALLING, handler=callback_in)

p2.irq(trigger=Pin.IRQ_FALLING, handler=callback_out)
