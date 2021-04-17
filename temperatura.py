# Complete project details at https://RandomNerdTutorials.com

from machine import Pin, ADC
from time import sleep
import dht
#from show import oled
from light_sensor import lum
from time import sleep

#pot = ADC(0)



#Pin(0, Pin.OUT).value(1)
sensor = dht.DHT11(Pin(2, Pin.IN, Pin.PULL_UP))
#sensor = dht.DHT11(Pin(14))
det = Pin(0, Pin.OUT)
count = 0
global on
on =  True
while True:
  count += 1
  try:
    sleep(2)
    result = lum()
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
#    valu = pot.read()

    temp_f = temp * (9/5) + 32.0
    print('Temperature: %3.1f C' %temp)
    print('Temperature: %3.1f F' %temp_f)
    print('Humidity: %3.1f %%' %hum)
    print('Lum: %3.1f Lu' %result)

    print('____________',count,'________________')
  #  oled.text('Temp: %3.1f C' %temp, 0, 10)
   # oled.text('Temp: %3.1f F' %temp_f, 0, 20)
    #oled.text('Hum: %3.1f %%' %hum, 0, 30)
    # oled.text('Lum: %3.1f Lu' %result, 0, 40)
   # oled.text('Val: %3.1f ' %valu, 0, 50)
  #  oled.show()
  except Exception  as e:
    print(e)
  finally:   
#    oled.fill(0)
    pass