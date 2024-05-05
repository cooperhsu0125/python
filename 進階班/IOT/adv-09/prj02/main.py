#########################匯入模組#########################
import mcu
from machine import Pin, I2C
import ssd1306
import time as t


#########################函式與類別定義#########################
def on_message(topic, msg):
    global mssg
    mssg = msg.decode("utf-8")
    topic = topic.decode("utf-8")
    oled.fill(0)
    oled.text(topic, 0, 10)
    oled.text(mssg, 0, 20)


#########################宣告與設定#########################
gpio = mcu.gpio()
i2c = I2C(scl=Pin(gpio.D1), sda=Pin(gpio.D2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
oled.fill(0)
wi = mcu.wifi("SingularClass", "Singular#1234")
wi.setup(ap_active=False, sta_active=True)
if wi.connect():
    oled.text(wi.ip, 0, 0)
MQTT = mcu.MQTT("mqtt.singularinnovation-ai.com", "cooper", "singular", "Singular#1234")
MQTT.connect()
MQTT.subscribe("cooper", on_message)
mssg = ""
#########################主程式#########################
while True:
    MQTT.check_msg()
    oled.show()
    t.sleep(0.1)
