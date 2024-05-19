#########################匯入模組#########################
import mcu
import time


#########################函式與類別定義#########################
def on_message(topic, msg):
    global mssg
    mssg = msg.decode("utf-8")
    topic = topic.decode("utf-8")


#########################宣告與設定#########################
gpio = mcu.gpio()
servo = mcu.servo(gpio.D8)
wi = mcu.wifi("SingularClass", "Singular#1234")
wi.setup(ap_active=False, sta_active=True)
if wi.connect():
    print(f"IP={wi.ip}")
mqtt_client = mcu.MQTT(
    "mqtt.singularinnovation-ai.com", "cooper", "singular", "Singular#1234"
)
mqtt_client.connect()
mqtt_client.subscribe("cooper", on_message)
mssg = 0
#########################主程式#########################
while True:
    mqtt_client.check_msg()
    servo.angle(int(mssg))
    time.sleep(1)
