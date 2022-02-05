'''

원의 면적과 원의 둘레를 구하는 프로그램을 작성하는데, PI = 3.141592 전역상수를 선언하고 상수를 활용.

'''

from math import pow

PI = 3.141592

#원의 면적을 구하는 함수
#원의 면적 = PI * 반지름^2
def circle_area(r:float) -> float:
    return round(PI * pow(r, 2), 2)

#원의 둘레를 구하는 함수
#원의 둘레 공식 : 2 * PI * 반지름
def circle_circumference(r:float) -> float:
    return round(2 * PI * r, 2)

#프로그램을 시작하는 함수
def main():
    radius = float(input("원의 반지름을 입력하세요:"))

    print(f"반지름이 {radius}인 원의 면적:{circle_area(radius)}, 원의 둘레:{circle_circumference(radius)}")

#프로그램의 시작을 알리는 함수 호출 
main()