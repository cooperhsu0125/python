#########################匯入模組#########################
from machine import Pin, PWM
from time import sleep

#########################函式與類別定義#########################

#########################宣告與設定#########################
frequency = 1000
duty_cycle = 0
led = PWM(Pin(2), freq=frequency, duty=duty_cycle)
a = 0
#########################主程式#########################
while True:
    for i in range(1024):
        a += 1
        led.duty(a)
        sleep(0.005)
    for i in range(1024):
        a -= 1
        led.duty(a)
        sleep(0.005)
