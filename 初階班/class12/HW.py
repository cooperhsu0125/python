import turtle as t

t.fillcolor("green")
t.pencolor("green")
t.shape('classic')
x = int(input('x:'))
y = int(input('y:'))
t.penup()
t.goto(x, y)
t.right(30)
t.pendown()
t.begin_fill()
a = 10
b = 5
for i in range(10, 31, 10):
    t.forward(a)
    t.right(150)
    t.forward(b)
    t.left(150)
    a += 10
    b += 5
t.setheading(0)
t.goto(x, y)
t.right(150)
a = 10
b = 5
for i in range(10, 31, 10):
    t.forward(a)
    t.left(150)
    t.forward(b)
    t.right(150)
    a += 10
    b += 5
t.left(150)
t.forward(45)
t.end_fill()
t.setheading(180)
t.forward(15)
t.fillcolor("brown")
t.pencolor("brown")
t.begin_fill()
t.left(90)
t.forward(7)
t.right(90)
t.forward(15)
t.right(90)
t.forward(7)
t.end_fill()
t.done()
