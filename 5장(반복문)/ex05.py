'''

for 문을 이용하여 팩토리얼(factorial)을 계산하는 프로그램 작성.
팩토리얼 n!은 1부터 n까지의 정수의 모두 곱한것을 의미하는 것이다.

'''

fact = 1
n = int(input("n에 해당하는 값을 입력하세요:"))

for i in range(fact, (n + 1)):
    fact *= i #fact = fac * i 를 복합대입연산자를 사용한 코드.

print("{}! = {} 입니다.".format(n, fact))

