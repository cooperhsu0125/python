#########################匯入模組#########################
from machine import Pin, I2C, ADC
import dht
import time
import mcu
import json
import ssd1306

#########################函式與類別定義#########################

#########################宣告與設定#########################
gpio = mcu.gpio()
wi = mcu.wifi("SingularClass", "Singular#1234")
wi.setup(ap_active=False, sta_active=True)
if wi.connect():
    print(f"IP={wi.ip}")
mqtt_client = mcu.MQTT(
    "mqtt.singularinnovation-ai.com", "cooper", "singular", "Singular#1234"
)
mqtt_client.connect()
i2c = I2C(scl=Pin(gpio.D1), sda=Pin(gpio.D2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
d = dht.DHT11(Pin(gpio.D0, Pin.IN))
light_sensor = ADC(0)
msg_json = {}
#########################主程式#########################
while True:
    d.measure()
    temp = d.temperature()
    hum = d.humidity()
    light_sensor_reading = light_sensor.read()
    oled.fill(0)
    oled.text(f"Humidity:{hum:02d}", 0, 0)
    oled.text(f"Temperature:{temp:02d}℃", 0, 10)
    oled.show()
    msg_json["humidity"] = hum
    msg_json["temperature"] = temp
    msg_json["light_sensor_reading"] = light_sensor_reading
    msg = json.dumps(msg_json)
    mqtt_client.publish("cooper", msg)
    time.sleep(1)
