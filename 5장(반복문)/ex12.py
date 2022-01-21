'''

while문의 실습
while 문은 조건을 정해놓고 반복을 하는 구조이다.

무한 루프를 조심하자!

'''

i = 0
while i < 5:
    print("반갑습니다.")
    i += 1
print("반복이 종료되었습니다.")

#숫자 0~9 까지 줄바꿈을 하지 아니하고 출력해보기(while문 사용)
i = 0
while i < 10:
    print(i, end = " ")
    i += 1

# 1~10까지의 누계합을 구하는 예제
print("-" * 10)
i = 0
sum = 0 
while i < 10:
    i += 1
    sum += i
    print(sum, end = " ")
    
# while 문을 사용하여 팩토리얼을 구하는 예제
print("-" * 10)

n = 5
f = 1
i = 1 

while i <= n:
    f *= i
    i += 1
print("{}! = {}".format(n, f))

# while 문을 사용하여 3단을 출력하는 예제
print("-" * 10)

n = 3
i = 0 
while i < 9:
    i += 1
    # % 뒤에 오는 숫자들은 출력할 때 자릿수 차지하게끔 만들어준다. %d, %2d
    # %.1f나 %0.1f나 동일한 자릿값을 출력한다 (소수점 첫째 자리만 나타내도록 한다.)
    print("{0} * {1} = {2:2d}".format(n, i, (n * i)))

print("-" * 10)
# 1 ~100 까지의 3의 배수만 누적값을 구하는 예제

i = 0
hap = 0

while i <= 100:
    i += 1
    if (i % 3) == 0:
        hap += i
print("1~100 사이 모든 3의 배수의 합은 {0}입니다.".format(hap))

print("-" * 10)
# 정수 안의 각 자리수의 합을 계산하는 예제
# ex) 1234라면 (1+2+3+4)를 계산

n = 1234
hap = 0

while n > 0 :
    hap += (n % 10) 
    n = n // 10

print("각 자리수의 합은 {0} 입니다.".format(hap))