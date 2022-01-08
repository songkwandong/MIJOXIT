'''

사용자로부터 두 개의 정수를 입력받아 두 수의 합을 구하는 프로그램을 만드는 방법

'''

x = int(input("첫 번째 정수를 입력하시오 : "))
y = int(input("두 번째 정수를 입력하시오 : "))


sum = x + y

diff = abs(x - y)

print("두 수의 합 : {}".format(sum))
print("두 수의 차 : {}".format(diff))

