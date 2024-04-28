#########################匯入模組#########################
import time as t
import mcu
from machine import Pin, ADC, PWM


#########################函式與類別定義#########################
def on_message(topic, msg):
    global mssg
    mssg = msg.decode("utf-8")
    topic = topic.decode("utf-8")
    print(f"my subscribe topic:{topic}, msg:{mssg}")


#########################宣告與設定#########################
wi = mcu.wifi("SingularClass", "Singular#1234")
wi.setup(ap_active=False, sta_active=True)
if wi.connect():
    print(f"IP={wi.ip}")
MQTT = mcu.MQTT("mqtt.singularinnovation-ai.com", "cooper", "singular", "Singular#1234")
MQTT.connect()
MQTT.subscribe("cooper", on_message)
mssg = ""
light_sensor = ADC(0)
frequency = 1000
duty_cycle = 0
gpio = mcu.gpio()
LED = mcu.LED(gpio.D5, gpio.D6, gpio.D7, True)
LED.R.duty(0)
LED.B.duty(0)
LED.G.duty(0)
#########################主程式#########################
while True:
    MQTT.check_msg()
    if mssg == "on":
        LED.R.duty(1023)
        LED.G.duty(1023)
        LED.B.duty(1023)
    elif mssg == "off":
        LED.R.duty(0)
        LED.B.duty(0)
        LED.G.duty(0)
    elif mssg == "auto":
        light_sensor_reading = light_sensor.read()
        a = light_sensor_reading
        if light_sensor_reading < 200:
            a = 0
        LED.R.duty(a)
        LED.G.duty(a)
        LED.B.duty(a)
    t.sleep(0.1)
