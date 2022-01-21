'''

사용자로부터 출력하고 싶은 구구단을 출력하는 프로그램 만들기

'''


gugudan_num = int(input("출력하고 싶은 구구단을 입력하세요(2~9):"))

for i in range(1, 10):
    if (gugudan_num < 2) or (gugudan_num > 9):
        print("단을 잘못 입력하였습니다. 조건 2~9")
        break
    result = gugudan_num * i
    print("{} X {} = {}".format(gugudan_num, i, result))
    

