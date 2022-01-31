'''

구의 부피를 계산하는 함수 sphere_volume()을 작성하여 보자.
그리고, 반지름을 사용자로부터 입력을 받고, 구의 부피를 구하는 함수를 호출해서 테스트

구의 부피 공식: 4/3 * pi * r의 세제곱

'''

from math import pi
from math import pow

#구의 부피를 구하는 함수를 선언 및 구현
def sphere_volume(r):
    return round((4.0/3.0) * pi * pow(r, 3),2)

r = float(input("구의 반지름을 입력하세요. :"))
print(f"구의 부피는 : {sphere_volume(r)} 입니다." )