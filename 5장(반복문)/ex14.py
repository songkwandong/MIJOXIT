'''

임의의 숫자를 맞추는 게임.

'''

from random import *

cnt = 0
rand_num = randint(1, 100)

print(rand_num)
print("기회는 10번입니다.")

while cnt < 10 :
    cnt += 1
    val = int(input("1~100까지의 임의의 숫자를 맞춰보세요:"))

    if val < rand_num:
        print("입력한 값이 더 낮습니다.")
    elif val > rand_num:
        print("입력한 값이 더 높습니다.")
    elif val == rand_num:
        print(f"딩동댕 시도 횟수는 {cnt}입니다.")
        continue_flag = input("게임을 계속하시겠습니까? (y는 계속, n은 중단) :")
        if continue_flag == "n":
            print("종료하겠습니다.")
            break
        else:
            print("게임을 재시작 합니다.")
            rand_num = randint(1, 100)
            cnt = 0
            continue
    print(f"남은 횟수는 {10-cnt} 입니다.")
    if (10 - cnt) == 0:
        print("10번안에 성공하지못하였습니다.")
    
    