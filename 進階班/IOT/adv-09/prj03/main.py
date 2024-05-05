#########################匯入模組#########################
import paho.mqtt.client as mqtt
import time as t


#########################函式與類別定義#########################
def on_publish(client, userdata, mid, reason_code, properties):
    print(f"Message{mid}has been published")


#########################宣告與設定#########################
client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.on_publish = on_publish
client.username_pw_set("singular", "Singular#1234")
client.connect("mqtt.singularinnovation-ai.com", 1883, 60)
client.loop_start()
#########################主程式#########################
while True:
    msg = input("輸入的訊息:")
    result = client.publish("cooper", msg)
    result.wait_for_publish()
    if result.rc == mqtt.MQTT_ERR_SUCCESS:
        print("Message publishre successfully")
    else:
        print("Failed to publish message")
    t.sleep(0.1)
