'''

1.증속, 2.감속, 3.중지 를 출력하고 사용자의 입력을 1,2,3 받아서
증속을 하면 속도를 10씩 증가하고 출력해준다.
감속을 하면 속도를 10씩 감소하고 출력해준다.
중지를 하면 플래그 변수를 이용하여 무한 루프를 빠져나간다.

'''

from operator import eq

end_flag = True
speed = 0 

while end_flag:
    user_input = input("입력해주세요. (증속 / 감속 / 중지):")
    if eq(user_input, "증속"):
        speed += 10
        print(f"선택은 {user_input} 현재 속도는 {speed}입니다.")
    elif eq(user_input, "감속"):
        speed -= 10
        if speed < 0:
            print("더 이상 감속할 수 없습니다.")
            speed = 0
        else:
            print(f"선택은 {user_input} 현재 속도는 {speed}입니다.")
    elif eq(user_input, "중지"):
        print(f"선택은 {user_input} 현재 속도는 {speed}입니다.")
        end_flag = False
    else:
        print("입력이 잘못되었습니다. 다시 입력해주세요.")
print(f"최종 속도는 {speed}입니다.")
