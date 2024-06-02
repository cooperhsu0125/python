#########################匯入模組#########################
import paho.mqtt.client as mqtt
import time
import getpass
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage


#########################函式與類別定義#########################
def on_publish(client, userdata, mid, reason_code, properties):
    print(f"Message {mid} has been published.")


#########################宣告與設定#########################
client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.on_publish = on_publish
client.username_pw_set("singular", "Singular#1234")
client.connect("mqtt.singularinnovation-ai.com", 1883, 60)
client.loop_start()
os.environ["OPENAI_API_KEY"] = getpass.getpass()
model = ChatOpenAI(model="gpt-4o", temperature=0.0)
#########################主程式#########################
while True:
    ans = input("請輸入想跟AI說的話: ")
    msg = model.invoke(
        [
            HumanMessage(
                content="""
    開燈是'ON'，關燈是'OFF'
    開門是'open'，關門是'close'
    你是一個負責開燈跟關燈的管理員以及開車庫門跟關車庫門的管理員
    你只能根據使用者的回應來決定要回答'ON'或'OFF'以及'open'或'close'
    不能回答其他的字串
                """
            ),
            HumanMessage(content=ans),
        ]
    ).content
    result = client.publish("cooper", msg)
    result.wait_for_publish()
    if result.rc == mqtt.MQTT_ERR_SUCCESS:
        print("Message published successfully")
    else:
        print("Failed to publish message")
    time.sleep(0.1)
