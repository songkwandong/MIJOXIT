'''

숫자 추측 게임을 만들기
파이썬에서는 ++ -- 와 같은 증감연산자는 사용하지 못한다.
대신 += -= 와 같은 증감연산자를 사용하자.
'''


from random import *

cnt = 0
rand_num = randint(1, 100)
print("난수는 {}입니다.".format(rand_num))

input_num = int(input("숫자를 맞춰보세요. (1~100)"))
while(True):
    cnt += 1

    if input_num == rand_num :
        print("정답입니다~ 게임을 종료합니다. 시도 횟수는 {}입니다.".format(cnt))
        break
    else:
        print("틀렸습니다. 다시 시도하세요~")
        if input_num > rand_num:
            print("입력한 숫자가 더 큽니다.")
        else:
            print("입력한 숫자가 더 작습니다.")
    input_num = int(input("숫자를 다시 입력해보세요 (1~100)"))
            