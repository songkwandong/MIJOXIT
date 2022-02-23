'''

원의 넓이와 둘레를 동시에 반환하는 함수를 작성하고 테스트
반지름은 사용자로부터 입력을 받는다.

넓이 PI * r^2
둘레 2PI * r
'''
from math import pi
from math import pow

def get_width_and_circumference(radius: float) -> tuple:
    width = pi * pow(radius, 2)
    circumference = 2 * pi * radius

    return (width, circumference)

if __name__ == "__main__":
    radius = float(input("원의 반지름을 입력하시오 : "))
    (width, circumference) = get_width_and_circumference(radius)
    print(f"원의 넓이는 {width}이고 원의 둘레는 {circumference}이다.")