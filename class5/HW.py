import turtle
"""
請使用turtle模組以及for印出以下圖形
t0_turtle_stamp.jpg
提示：
turtle.home()是讓烏龜回到原點的指令
"""

turtle.penup()
turtle.goto(90, 0)
turtle.stamp()
turtle.goto(65, 65)
turtle.left(45)
turtle.stamp()
turtle.goto(0, 90)
turtle.left(45)
turtle.stamp()
turtle.goto(-65, 65)
turtle.left(45)
turtle.stamp()
turtle.goto(-90, 0)
turtle.left(45)
turtle.stamp()
turtle.goto(-65, -65)
turtle.left(45)
turtle.stamp()
turtle.goto(0, -90)
turtle.left(45)
turtle.stamp()
turtle.goto(65, -65)
turtle.left(45)
turtle.stamp()
turtle.home()
for a in range(8):
    turtle.left(45 * a)
    turtle.forward(100)
    turtle.stamp()
    turtle.home()
turtle.done()
