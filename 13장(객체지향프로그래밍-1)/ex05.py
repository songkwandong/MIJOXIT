'''

원을 클래스로 표시해보자.
원은 반지름(radius)을 가지고 있다
원의 넓이와 둘레를 계산하는 메소드를 정의해보자
생성자는 매개변수가 존재하는 생성자를 만들어보자

출력결과
원의 반지름 : 10
원의 넓이 : 314.16 r^2*pi
원의 둘레 : 62.83 2*pi*r

'''

from math import pi

class Circle:
    __radius = 0
    __area = 0
    __circumference = 0

    def __init__(self, radius):
        self.__radius = radius

    def cal_area(self):
        self.set_area(round(self.__radius * self.__radius * pi, 2))
    def cal_circumference(self):
        self.set_circumference(round(2 * self.__radius * pi, 2))

    def __str__(self):
        print(f"원의 반지름 :{self.get_radius()}")
        print(f"원의 넓이 :{self.get_area()}")
        print(f"원의 둘레 :{self.get_circumference()}")

    def get_radius(self):
        return self.__radius
    def get_area(self):
        return self.__area
    def get_circumference(self):
        return self.__circumference

    def set_area(self, area):
        self.__area = area
    def set_circumference(self, circum):
        self.__circumference = circum


if __name__ == "__main__":
    circle1 = Circle(10)
    circle1.cal_area()
    circle1.cal_circumference()
    circle1.__str__()
    