'''

super() 메서드 : 자손클래스에서 메서드 오버라이딩을 할 때, 
조상클래스의 메서드나 필드를 사용해야 되는 경우가 종종 있다.

이럴 때 사용하는 것이 바로
super() 메서드


'''

class Car:
    value = "조상클래스 필드값"
    def car_method(self):
        print("조상클래스 메서드 호출")

class Sedan(Car):
    value = "자손클래스 필드값"
    def car_method(self):
        super().car_method()
        print("자손클래스 메서드 호출")
        print(f"조상클래스의 value 값: {super().value}")
        print(f"자손클래스의 value 값: {self.value}")
    
if __name__ == "__main__":
    sedan = Sedan()
    sedan.car_method()