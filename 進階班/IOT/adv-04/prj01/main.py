#########################匯入模組#########################
from machine import Pin, ADC, PWM
from time import sleep
import mcu

#########################函式與類別定義#########################

#########################宣告與設定#########################
gpio = mcu.gpio()
light_sensor = ADC(0)
frequency = 1000
duty_cycle = 0
a = 0
R = PWM(Pin(gpio.D5), freq=frequency, duty=duty_cycle)
G = PWM(Pin(gpio.D6), freq=frequency, duty=duty_cycle)
B = PWM(Pin(gpio.D7), freq=frequency, duty=duty_cycle)

#########################主程式#########################
while True:
    light_sensor_reading = light_sensor.read()
    a = light_sensor_reading
    if light_sensor_reading < 400:
        a = 0
    R.duty(a)
    G.duty(a)
    B.duty(a)
