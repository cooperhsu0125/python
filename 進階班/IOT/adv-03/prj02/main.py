#########################匯入模組#########################
from machine import Pin, PWM
from time import sleep
import mcu

#########################函式與類別定義#########################

#########################宣告與設定#########################
frequency = 1000
duty_cycle = 0
a = 0
gpio = mcu.gpio()
R = PWM(Pin(gpio.D5), freq=frequency, duty=duty_cycle)
G = PWM(Pin(gpio.D6), freq=frequency, duty=duty_cycle)
B = PWM(Pin(gpio.D7), freq=frequency, duty=duty_cycle)
#########################主程式#########################
while True:
    for i in range(1024):
        a += 1
        b = 1023 - a
        G.duty(a)
        R.duty(b)
        sleep(0.005)
    a = 0
    for i in range(1024):
        a += 1
        b = 1023 - a
        B.duty(a)
        G.duty(b)
        sleep(0.005)
    a = 0
    for i in range(1024):
        a += 1
        b = 1023 - a
        R.duty(a)
        B.duty(b)
        sleep(0.005)
    a = 0
