'''

사용자로부터 2개의 정수 값을 입력받고 첫 번째 입력받은 값부터 두 번째 입력받은 값 까지의 범위에서 3의 배수이고, 4의 배수를 제외하고 출력하는 프로그램을 
작성하시오

반복문의 
break - 바로 나감.
continue - 밑의 코드를 수행하지않고 다음 루프로 감.

'''

first_num = int(input("첫 번째 정수 값을 입력해주세요:"))
second_num = int(input("두 번째 정수 값을 입력해주세요:"))

for i in range(first_num, second_num + 1):
    # if (i % 3 != 0) and (i % 4 != 0):
    #     print(i)
    if (i % 3) == 0 and (i % 4) == 0:
        continue
    print(i)