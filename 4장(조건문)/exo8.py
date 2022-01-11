'''

사용자로부터 두 개의 정수를 입력받아서 둘 중에서 큰 수를 출력하는 프로그램

'''

try_cnt=2
bigger_num=0

for i in range(0,try_cnt):
    input_num = int(input("정수를 입력해주세요 :"))
    print("남은 횟수 : {}".format(try_cnt - (i + 1)))
    if bigger_num < input_num:
        bigger_num = input_num

print("입력한 수 중 젤 큰 수는 {}입니다.".format(bigger_num))
