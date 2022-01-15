'''

사용자로부터 달을 입력받아서 입력한 달의 일수를 구하는 프로그램을 작성하기.

'''

month = int(input("월을 입력하세요:"))
day = 0

if month == 2:
    day = 28
elif (month == 4) or (month == 6) or (month == 9) or (month == 11):
    day = 30
else:
    day = 31

print("{}월의 일수는 {}일 입니다.".format(month, day))