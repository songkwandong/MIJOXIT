'''

간단한 사칙연산 계산기 만들기

'''

#더하기 함수
def add(x, y):
    return x + y

#빼기 함수
def substract(x, y):
    return x - y

#곱하기 함수
def multiply(x, y):
    return x * y

#나누기 함수
def divide(x, y):
    return round((x / y), 2)

#연산자에 의해서 분기를 시킨다.
temp = "y"
while True:
    if temp == "n":
        print("종료하겠습니다..")
        break
    elif temp == "y": 
        x = float(input("숫자 1를 입력해주세요:"))
        y = float(input("숫자 2를 입력해주세요:"))
        op = input("원하는 연산을 입력하세요 (+,-,*,/) :")

        if op == "+":
            print(add(x, y))
        elif op == "-":
            print(substract(x, y))
        elif op == "*":
            print(multiply(x, y))    
        elif op == "/":
            print(divide(x, y))
        else:
            print("연산자를 잘 못 입력하였습니다.")    
    else:
        print("y/n으로 입력해주세요.")
        
    temp = input("계산을 다시 하시겠습니까? y/n :")
    