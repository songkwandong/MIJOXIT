'''

생성자에 대한 실습
개념 : 인스턴스를 생성하기 위해 꼭 필요한 존재
아울러 필드의 초기화 메서드 역할을 한다.
__init__() 작성해줌으로써 생성자가 호출이 된다.
만약에 클래스에 생성자가 존재하지않으면 인터프리터가 알아서 하나의 기본생성자를 추가


'''

class Person:
    __name = "" # __를 붙이면 private 성질은 클래스 내부에서만 접근 가능하다.
    #외부에서 접근이 불가.
    #__가 붙지 아니하면 public 성질은 지닌다. 클래스 내부,외부 모두 접근 가능.
    age = 0
    height = 0
    weight = 0
    address = ""
    #기본생성자 작성

    def __init__(self):
        self.__name = "송관동"
        self.age = 29
        self.height = 171
        self.weight = 80
        self.address = "광명"
        print("Person의 기본 생성자 호출")
    #getter() 는 리턴값만 존재하고 매개변수는 존재하지않는다.
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.age
    def get_height(self):
        return self.height
    def get_weight(self):
        return self.weight
    def get_address(self):
        return self.address

    #setter() 메서드
    def set_name(self, name):
        self.__name = name
    def set_age(self, age):
        self.age = age
    def set_height(self, height):
        self.height = height
    def set_weight(self, weight):
        self.weight = weight
    def set_address(self, address):
        self.address = address

    #__str__() 멤버변수의 값을 간단하게 확인하고자 할 때 사용하면
    #편리 자바언어의 toString()와 유사.
    def __str__(self):
        print(self.__name)
        print(self.age)
        print(self.weight)
        print(self.height)
        print(self.address)

