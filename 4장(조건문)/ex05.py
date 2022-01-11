'''

사용자에게 명령어를 입력받아서 터틀그래픽을 제어.
즉, 사용자가 문자열로 "left"를 입력을 하면 왼쪽으로 회전하게 되고, 사용자가 "right" 를 입력했다면 오른쪽으로 회전하게 하는 프로그램.

turtle.exitonclick()
터틀 그래픽 창이 클릭이 되어야 사라지게되는 코드.

'''

import turtle

t = turtle.Pen()

while True:
    from_user_order = input("이동할 방향을 입력해주세요(왼쪽=left, 오른쪽=right, 종료=quit) 입력:")
    if from_user_order == "quit":
        print("멈추겠습니다...")
        break
    elif from_user_order == "left":
        print("left를 입력하셨습니다...")
        t.left(60)
        t.forward(50)
    elif from_user_order == "right":
        print("right를 입력하셨습니다...")
        t.right(60)
        t.forward(50)
    else: 
        print("다시 입력해주세요(왼쪽=left, 오른쪽=right, 종료=quit)")

turtle.exitonclick()
