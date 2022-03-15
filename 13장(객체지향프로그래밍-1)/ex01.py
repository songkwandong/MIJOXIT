'''

객치지향 프로그래밍(OOP : Object Oriented Programming)
현실 세계에 있는 어떠한 사물을 코드로 표현하는 방법
클래스 용어 : 사물을 묘사하는 것이고 예를 들면 설계도, 붕어빵 틀.
클래스 요소 : 멤버변수(필드, 속성), 멤버 메서드(기능), 생성자(필수)


Car 클래스 설계하기
'''


class Car:
    # Car 클래스의 필드
    color = ""
    speed = 0
    # Car 클래스의 기능을 담당하는 메소드
    # 속도 높이는 메소드

    def up_speed(self, speed):
        #self는 자바에서 this와 동일하며 자기 자신의 주소를 가지고 있는 인자다
        # 인스턴스를 생성해야 비로소 self는 활성화 된다.
        if speed < 0:
            print("속도는 음수일수가 없습니다. ")
            return
        else:
            self.speed += speed

    # 속도 높이는 메소드
    def down_speed(self, speed):
        if (self.speed - speed) < 0 or speed < 0:
            print("속도는 음수일수가 없습니다. ")
            return
        else:
            self.speed -= speed

    # 멤버변수(필드)의 값을 출력해주는 메소드 추가.
    def print_fields(self, my_car):
        print(f"{my_car}의 색상 : {self.color}, 속도(감속/증속) : {self.speed}K/M")    

if __name__ == "__main__":
    # Car 클래스의 인스턴스를 생성하여 사용하기
    my_car_1 = Car()
    my_car_2 = Car()
    my_car_3 = Car()

    #아래와 같이 주소를 찍어보면 각각 인스턴스는 독립적인 공간을 지니고 있다.
    print(f"my_car_1의 주소 :f{id(my_car_1)}")
    print(f"my_car_2의 주소 :f{id(my_car_2)}")
    print(f"my_car_3의 주소 :f{id(my_car_3)}")

    print(f"my_car_1의 타입 :f{type(my_car_1)}")
    print(f"my_car_2의 타입 :f{type(my_car_2)}")
    print(f"my_car_3의 타입 :f{type(my_car_3)}")

    my_car_1.color = "파랑색"
    my_car_1.up_speed(50)
    my_car_1.print_fields("my_car_1")
    
    my_car_2.color = "노란색"
    my_car_2.up_speed(100)
    my_car_2.down_speed(100)
    my_car_2.print_fields("my_car_2")
    
    my_car_3.color = "빨강색"
    my_car_3.up_speed(-100)
    my_car_3.up_speed(100)
    my_car_3.down_speed(100)
    my_car_3.down_speed(100)
    my_car_3.print_fields("my_car_3")

#클래스를 설계하고 사용하는 루틴
#1.클래스를 설계(정의)
#2.인스턴스 생성하기
#3.필드나 메소드를 호출하여 원하는 프로그램을 만들기.