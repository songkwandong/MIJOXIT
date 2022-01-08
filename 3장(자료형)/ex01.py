'''

파이썬에서의 자료형(Data-type)

'''
from math import *

print(type(17))
print(type(10.77779))
print(type("hi"))

#반지름이 r인 구의 부피는 ? 4/3 * PI * r의 세제곱
#반지름 = 5인 구의 부피를 계산하는 프로그램

r = 5.0

#volume = (4.0/3.0) * pi * (r ** 3)
volume = (4.0/3.0) * pi * pow(r, 3)

#print("반지름이 {}인 구의 부피는 : {}".format(r, volume))

#구의 겉넓이의 공식 : 4 * pi * r의 제곱

outer_area = 4.0 * pi * (r ** 2)
print("반지름이 {}인 구의 겉넓이는 : {}".format(r, outer_area))