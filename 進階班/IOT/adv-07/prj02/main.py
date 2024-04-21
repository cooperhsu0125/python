#########################匯入模組#########################
from umqtt.simple import MQTTClient
import sys
import time as t
import mcu
from machine import Pin, ADC, PWM


#########################函式與類別定義#########################
def on_message(topic, msg):
    global mssg
    mssg = msg.decode("utf-8")
    topic = topic.decode("utf-8")
    print(f"my subscribe topic:{topic}, msg:{mssg}")
    if mssg == "on":
        led.duty(0)
    elif mssg == "off":
        led.duty(1023)


#########################宣告與設定#########################
wi = mcu.wifi("SingularClass", "Singular#1234")
if wi.connect():
    print(f"IP={wi.ip}")
mq_sever = "mqtt.singularinnovation-ai.com"
mqttClientID = "cooper"
mqtt_username = "singular"
mqtt_password = "Singular#1234"
mqClient0 = MQTTClient(
    mqttClientID, mq_sever, user=mqtt_username, password=mqtt_password, keepalive=30
)
try:
    mqClient0.connect()
except:
    sys.exit()
finally:
    print("connected MQTT sever")
mqClient0.set_callback(on_message)
mqClient0.subscribe("cooper")
mssg = ""
light_sensor = ADC(0)
frequency = 1000
duty_cycle = 0
led = PWM(Pin(2), freq=frequency, duty=duty_cycle)
#########################主程式#########################
while True:
    mqClient0.check_msg()
    mqClient0.ping()

    if mssg == "auto":
        light_sensor_reading = light_sensor.read()
        a = light_sensor_reading
        if light_sensor_reading < 400:
            a = 0
        led.duty(1023 - a)
    t.sleep(0.1)
