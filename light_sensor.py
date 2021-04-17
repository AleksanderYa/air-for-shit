import bh1750
from machine import I2C,Pin

def lum():
    i2c = I2C(Pin(5), Pin(4))
    result = bh1750.sample(i2c) # in lux
    print(result)
    return result

lum()