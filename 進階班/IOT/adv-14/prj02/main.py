#########################匯入模組#########################
import mcu
from machine import ADC, Pin
import json
import dht
import time


#########################函式與類別定義#########################
def on_message(topic, msg):
    global mssg
    mssg = msg.decode("utf-8")
    topic = topic.decode("utf-8")


#########################宣告與設定#########################
gpio = mcu.gpio()
light_sensor = ADC(0)
d = dht.DHT11(Pin(gpio.D0, Pin.IN))
servo = mcu.servo(gpio.D8)
R = Pin(gpio.D5, Pin.OUT)
G = Pin(gpio.D6, Pin.OUT)
B = Pin(gpio.D7, Pin.OUT)
wi = mcu.wifi("SingularClass", "Singular#1234")
wi.setup(ap_active=False, sta_active=True)
if wi.connect():
    print(f"IP={wi.ip}")
MQTT = mcu.MQTT(
    "mqtt.singularinnovation-ai.com", "cooper_H", "singular", "Singular#1234"
)
MQTT.connect()
MQTT.subscribe("cooper_AI", on_message)
mssg = ""
msg_json = {}
R.value(0)
B.value(0)
G.value(0)
light = 0
door = 0
#########################主程式#########################
while True:
    MQTT.check_msg()
    d.measure()
    temp = d.temperature()
    hum = d.humidity()
    light_sensor_reading = light_sensor.read()
    msg_json["humidity"] = hum
    msg_json["temperature"] = temp
    msg_json["light_sensor_reading"] = light_sensor_reading
    if mssg == "on":
        R.value(1)
        B.value(1)
        G.value(1)
        light = 1
    elif mssg == "off":
        R.value(0)
        B.value(0)
        G.value(0)
        light = 0
    if mssg == "open":
        servo.angle(180)
        door = 1
    elif mssg == "close":
        servo.angle(0)
        door = 0
    msg_json["light"] = light
    msg_json["door"] = door
    msg = json.dumps(msg_json)
    MQTT.publish("cooper_H", msg)
    time.sleep(1)
