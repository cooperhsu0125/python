#########################匯入模組#########################
import network

#########################函式與類別定義#########################

#########################宣告與設定#########################
wlan = network.WLAN(network.STA_IF)  # STA:連線
ap = network.WLAN(network.AP_IF)  # AP:分享
ap.active(False)
wlan.active(True)

wifi_list = wlan.scan()
print("Scan result:")
for i in range(len(wifi_list)):
    print(wifi_list[i])
wlSSID = "SingularClass"
wlPWD = "Singular#1234"
wlan.connect(wlSSID, wlPWD)
while not (wlan.isconnected()):
    pass
print("connect succesfully", wlan.ifconfig())
#########################主程式#########################
