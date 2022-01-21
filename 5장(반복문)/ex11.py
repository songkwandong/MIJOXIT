'''

'''

import turtle

t = turtle.Pen()

x = 20

for i in range(20):
    t.left(10)
    for i in range(4):
        t.forward(200)   
        t.left(90)

turtle.exitonclick()