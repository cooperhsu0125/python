#########################匯入模組#########################
from machine import Pin
from time import sleep
import mcu

#########################函式與類別定義#########################

#########################宣告與設定#########################
gpio = mcu.gpio()
R = Pin(gpio.D5, Pin.OUT)
G = Pin(gpio.D6, Pin.OUT)
B = Pin(gpio.D7, Pin.OUT)

R.value(0)
B.value(0)
G.value(0)
#########################主程式#########################
while True:
    R.value(1)

    G.value(0)
    sleep(1)
    G.value(1)
    sleep(1)
    R.value(0)

    G.value(1)
    sleep(1)
