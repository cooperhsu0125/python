#########################匯入模組#########################
import time
import mcu

#########################函式與類別定義#########################

#########################宣告與設定#########################
wi = mcu.wifi("SingularClass", "Singular#1234")
wi.setup(ap_active=False, sta_active=True)
if wi.connect():
    print(f"IP={wi.ip}")
mqtt_client = mcu.MQTT(
    "mqtt.singularinnovation-ai.com", "cooper", "singular", "Singular#1234"
)
mqtt_client.connect()
#########################主程式#########################
while True:
    msg = input("message")
    mqtt_client.publish("cooper", msg)
    time.sleep(0.1)
