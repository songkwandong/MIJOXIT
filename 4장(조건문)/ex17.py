'''

사용자로부터 정수를 입력받아서 음수, 0 , 양수 중에 어떤 값인지를 출력하는 프로그램.


'''

input_num = int(input("정수를 입력해주세요. :"))

if input_num >= 0:
    print("양수입니다.")
elif input_num == 0:
    print("0입니다.")
else:
    print("음수입니다.")
