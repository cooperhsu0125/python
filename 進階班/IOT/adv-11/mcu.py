import network
from machine import Pin, PWM
from umqtt.simple import MQTTClient
import sys


class gpio:
    def __init__(self):
        self._D0 = 16
        self._D1 = 5
        self._D2 = 4
        self._D3 = 0
        self._D4 = 2
        self._D5 = 14
        self._D6 = 12
        self._D7 = 13
        self._D8 = 15
        self.SDD3 = 10
        self.SDD2 = 9

    @property
    def D0(self):
        return self._D0

    @property
    def D1(self):
        return self._D1

    @property
    def D2(self):
        return self._D2

    @property
    def D3(self):
        return self._D3

    @property
    def D4(self):
        return self._D4

    @property
    def D5(self):
        return self._D5

    @property
    def D6(self):
        return self._D6

    @property
    def D7(self):
        return self._D7

    @property
    def D8(self):
        return self._D8


class wifi:
    def __init__(self, ssid=None, password=None):
        self.sta = network.WLAN(network.STA_IF)  # STA:連線
        self.ap = network.WLAN(network.AP_IF)  # AP:分享
        self.ssid = ssid
        self.password = password
        self.ap_active = False
        self.sta_active = False
        self.ip = None

    def setup(self, ap_active=False, sta_active=False):
        # 使用方法:wi.setup(ap_active=True|False,sta_active=True|False)# | 是或
        self.ap_active = ap_active
        self.sta_active = sta_active
        self.ap.active(ap_active)
        self.sta.active(sta_active)

    def scan(self):
        if self.sta_active:
            wifi_list = self.sta.scan()
            print("Scan result:")
            for i in range(len(wifi_list)):
                print(wifi_list[i][0])
        else:
            print("sta未啟動")

    def connect(self, ssid=None, password=None) -> bool:
        ssid = ssid if ssid is not None else self.ssid
        password = password if password is not None else self.password
        if not self.sta_active:
            print("sta未啟動")
            return False
        if ssid is None or password is None:
            print("wifi名稱或密碼未設定")
            return False
        self.sta.connect(ssid, password)
        if self.sta_active:
            self.sta.connect(ssid, password)
            while not self.sta.isconnected():
                pass
            self.ip = self.sta.ifconfig()[0]
            print("connect successfully", self.sta.ifconfig())
            return True


class LED:
    def __init__(self, r_pin, g_pin, b_pin, pwm: bool = False):
        if pwm == False:
            self.R = Pin(r_pin, Pin.OUT)
            self.G = Pin(g_pin, Pin.OUT)
            self.B = Pin(b_pin, Pin.OUT)
        else:
            frequency = 1000
            duty_cycle = 0
            self.R = PWM(Pin(r_pin), freq=frequency, duty=duty_cycle)
            self.G = PWM(Pin(g_pin), freq=frequency, duty=duty_cycle)
            self.B = PWM(Pin(b_pin), freq=frequency, duty=duty_cycle)


class MQTT:
    def __init__(self, mq_sever, mqttClientID, mqtt_username, mqtt_password):
        self.mq_sever = mq_sever
        self.mqttClientID = mqttClientID
        self.mqtt_username = mqtt_username
        self.mqtt_password = mqtt_password
        self.client = MQTTClient(
            mqttClientID,
            mq_sever,
            user=mqtt_username,
            password=mqtt_password,
            keepalive=30,
        )

    def connect(self):
        try:
            self.client.connect()
        except:
            sys.exit()
        finally:
            print("connected MQTT sever")

    def subscribe(self, topic: str, on_msg):
        self.client.set_callback(on_msg)
        self.client.subscribe(topic)

    def check_msg(self):
        self.client.check_msg()
        self.client.ping()

    def publish(self, topic: str, msg: str):
        topic = topic.encode("utf-8")
        msg = msg.encode("utf-8")
        self.client.publish(topic, msg)


class servo:
    def __init__(self, sg_pin):
        self.sg = PWM(Pin(sg_pin), freq=50)

    def angle(self, angle: int):
        if 0 <= angle <= 180:
            self.sg.duty(int(1023 * (0.5 + angle / 90) / 20))
