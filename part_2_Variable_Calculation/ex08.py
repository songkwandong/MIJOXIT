'''

내장 함수 및 math 라이브러리 함수 이용

모듈 호출시 import
라이브러리 호출시 from x import x
'''
from math import *


print(abs(-77))
print(abs(77))

#반올림
print(round(1.222))
print(round(1.522))

#주어진 매개 변수 중 최대값 구하기.
print(max(10, -20, 100, 9999))

#주어진 매개 변수 중 최솟값 구하기.
print(min(10, -20, 100, 9999))

#sqrt = 제곱근
print(sqrt(4.0))

#연산자 **와 동일.
print(pow(3, 2))