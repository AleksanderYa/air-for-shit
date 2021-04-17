from machine import Pin
from machine import RTC
#from machine import ADC
from time import sleep
from light_sensor import lum
import dht
import time

# Устанавливаем уровень влажности 
humiditty = 60 # %

# Константы
TIME_LIGHT = []
TIME_OFF = []
SHIT = False
LIGHT_ON = False
TIMER = False
WHILE = True # Константа для цикла всей проги
# Инициализация пинов
vannaya = Pin(12, Pin.OUT) #инициализация выхода на реле вентилятора в ванной
vannaya.value(1) # отключаем вентилятор, так как при инициализации
                 # подается на выход минус и это вкл вентилятор
tualet = Pin(14, Pin.OUT) #инициализация выхода на реле вентилятора в туалете
tualet.value(1) # тоже что и для ванной
                 
vihod = Pin(13, Pin.OUT) #инициализация выхода на реле вентилятора выхода в шахту
vihod.value(1)  # тоже что и для ванной

button = Pin(16, Pin.IN) # инициалицазия кнопки  

def time_is():
    '''
    Функция возвращает теперешнее время в вормате list [12, 44]
    '''
    try:
        rtc = RTC() # инициал
        h = rtc.datetime()[4] + 2 # + 2 часа к поясу
        m = rtc.datetime()[5] # минуты
        tm = str(h) + ':' + str(m) 
        print(tm)
        return [h, m] 
    except Exception as e:
        err() 
        print(e)
    
def rec_time():
    '''
    Возвращает разницу в минутах от заданого времени в констатне и в данный момент
    '''
    try:
        #    global TIME_LIGHT
        if (time_ist[0] - TIME_LIGHT[0]) == 1: # если изменилось время в часах
            t_now[1] += 60 # добавляем час к теперешним минутам 
            res = time_ist[1] - TIME_LIGHT[1] # разница в минутах 
            print('(res_time)res1-',res)
            return res
        elif (time_ist[0] - TIME_LIGHT[0]) == 0: # если нет изменения в часах
            res = time_ist[1] - TIME_LIGHT[1] # просто разниуа в минутах
            print('(res_time)res0-',res)
            return res
        else:
        #        TIME_LIGHT = time_is()
        #        print(TIME_LIGHT)
            return 0 # возрат ноля если что дугое
    except Exception as e:
        err()
        print(e)


def humm():
    '''
    Возвращает влажность с датчика от 0 до 95...
    '''
    try:
        sensor = dht.DHT11(Pin(0, Pin.IN, Pin.PULL_UP)) # инициалицация сенсора
        sleep(1) # спим сикунду что бы собрать более точные данные
        sensor.measure() # что то там важное, толи сбор данных с датчика
        hum =  sensor.humidity() # конкретно влажность
        return hum
    except Exception as e:
        err()
        print(e)

def err(col=5):
    '''
    В случае сработки ошибки мигает светодиод на плате
    '''
    try:
        led = Pin(2, Pin.OUT) #  инициалицация пина для леда
        for i in range(col): # сколько раз микнет, по стандарту 5 раз
            led.value(1)
            sleep(0.5)
            led.value(0)
            sleep(0.5)
            led.value(1)
            sleep(0.5)
    except Exception as e:
        err()
        print(e)

def if_light():
    '''
    Преакция на свет
    '''
    try:
        global TIME_LIGHT # меняем константы
        global LIGHT_ON
        if lum() > 20 and not LIGHT_ON:  # если сработал датчик света и константа Фолс
            TIME_LIGHT = time_ist # обнулим время в константе
            LIGHT_ON = True
#            tualet.value(0)
            vihod.value(0) # влючаем выход
            print('if_light', TIME_LIGHT)
        elif lum() < 20 and hum < humiditty: # если свет выключили и влажность низкая
            LIGHT_ON = False # выкл
            vihod.value(1) # выключаем  выход
            tualet.value(1) # выкл туалет
            vannaya.value(1) # выкл ванную
            SHIT = False # выключаем константу на доп винтелятор
            TIME_LIGHT = time_ist # обнуляем время константе
            print('elif_light ', TIME_LIGHT)
            sleep(5) # спим что бы была задержка после выключения
        elif lum() < 20 and hum > humiditty: # если свет выключили и влажность высокая
            LIGHT_ON = False
            SHIT = False
            tualet.value(1)
            TIME_LIGHT = time_ist
            print('elif_light ', TIME_LIGHT)
            sleep(5) 
            
    except Exception as e:
        err()
        print(e)
    
def shit():
    '''
    Включает дополнительно винтелятор в ванной и туалете если свет горт больше 4 мин.
    '''
    try:
        global SHIT # глобально
        if rec_time() >= 4: # если функция возвращает разницу во времени и она большеравно 4 мин ок
            SHIT = True # вкл константу на то что ктото какает
            tualet.value(0) # вкл туалет 
            vannaya.value(0) # включаем ванную
    except Exception as e:
        err()
        print(e)    
    
    
def if_hum():
    '''
    Если есть влажность включает и выключает вентели
    '''
    try:
        global SHIT
        print('(if_hum)Humidity-', type(hum), hum)
        if hum > humiditty: # если есть влажность больше заданой
            vannaya.value(0) # вкл ванная
            vihod.value(0)  # вкл вых
            tualet.value(0)  # вкл туалет
            
        elif hum < humiditty and lum() < 20: # если нет влажности и нет света
            vihod.value(1) # выкл выход
            tualet.value(1) # выкл туалет
            vannaya.value(1) # выкл выход
            SHIT = False # отключает кончтанту
            sleep(5) # задержка
        elif hum < humiditty and lum() > 20 and not SHIT: # если влажности нет но есть свет 
            vannaya.value(1) # выключаем ванную
    except Exception as e:
        err()
        print(e)   

def start_timer():
    try:
        TIMER = True
        timer_time()
        timer()
    except Exception as e:
        err()
        print(e)
"""    
def timer_time():
    time = time_ist
     

def timer():
    try:
        global TIMER
        if TIME_OFF == time_ist and TIMER: # если время совпадает с установленным и  тру константа 
            if lum() < 10 and hum > humiditty: # если нет света и есть влага 
        #            vihod.value(1) # выкл выход 
                tualet.value(1)
        #            vannaya.value(1)
                TIMER = False
            elif lum() < 10 and hum < humiditty: # если   нет света и нет влаги
        #            vihod.value(1) # выкл выход 
                tualet.value(1)
        #            vannaya.value(1)
                TIMER = False
            else:
                TIMER = False
    except Exception as e:
        err()
        print(e)
        
"""
def butt():
    try:
        if button.value() == 1:
            global WHILE
            WHILE = False
    except Exception as e:
        err()
        print(e)
        
while WHILE:
    hum = humm()
    time_ist = time_is()
    if_light()
    if_hum()
    butt()
    shit()
   
print('end')
tualet.value(1)
vihod.value(1)
vannaya.value(1)
