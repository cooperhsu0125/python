"""
請使用turtle模組、for、time模組來印出時鐘的秒針
基本功能參考影片t1_turtle_time.mp4
提示：
turtle.clear() # 清空畫面指令
import time  # 匯入time模組
time.sleep(1) # 延遲1秒
"""
import turtle
import time

turtle.speed(1000)
for a in range(60):
    turtle.left(90 - 6 * a)
    turtle.forward(100)
    turtle.home()
    time.sleep(1)
    turtle.clear()
turtle.done()
