'''

터틀 그래픽을 활용하여 별 모양을 그려보는 프로그램을 작성.

'''

import turtle 

t = turtle.Pen()

for i in range(0, 5):
    t.forward(200)   
    t.right(144)

turtle.exitonclick()