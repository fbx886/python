import turtle as t
import time as ti
s = 0
while True:
    t.goto(0, 0)
    t.penup()
    t.pencolor("red")
    t.fillcolor("red")
    t.pendown()
    t.right(45)
    t.begin_fill()
    for i in range(4):
        t.forward(100)
        t.right(90)
    t.end_fill()
    t.right(90)
    t.begin_fill()
    t.circle(50)
    t.right(90)
    t.circle(50)
    t.end_fill()
    ti.sleep(5)
    t.reset()