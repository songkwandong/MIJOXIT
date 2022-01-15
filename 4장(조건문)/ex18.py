'''

주사위 눈을 랜덤으로 발생시켜서 해당하는 숫자를 출력하는 프로그램을 만들기

randint(a, b) a~b 사이의 임의의 int값을 반환해주는 함수 사용하여 프로그램 작성
random() 함수는 0.0~1 미만의 임의의 float값을 반환
randrange(start, stop, step) 함수는 start에서 stop까지 step의 값에따라서 임의의 수를 반환
randrange(n) 0~n 까지의 임의의 정수값을 반환.

'''
from random import *

for i in range(0, 10):
    print("주사위 값은 {}입니다.".format(randint(1, 6)))
print("-" * 40)

# for i in range(0, 10):
#     print("주사위 값은 {}입니다.".format(random()))
# print("-" * 40)

for i in range(0, 10):
    print("주사위 값은 {}입니다.".format(randrange(0, 6, 1)))
print("-" * 40)

for i in range(0, 10):
    print("주사위 값은 {}입니다.".format(randrange(6)))
print("-" * 40)
