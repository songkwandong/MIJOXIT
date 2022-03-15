'''

매개변수가 있는 생성자에 대한 실습

'''


from turtle import color


class Monitor:
    #필드 선언
    __company = ""
    __inch = 0
    __price = 0
    __color = ""

    # 파이썬에서는 1개 이상의 생성자를 만들수가 없다.
    # 오버로딩 : 같은 메서드명으로 다른 일을 하게끔 만드는 작업
    # 매개변수의 타입과 개수에 따라서 같은 이름의 메서드라도 다른 메서드가 호출이 되는
    # 형태를 지칭.
    # def __init__(self):
    #     print("기본 생성자 호출")

    # 매개 변수가 4개인 생성자.
    def __init__(self, company, inch, price, color):
        #self. company는 멤버변수를 칭함.
        #company는 외부에서 생성자를 호출할 때 매개변수 값으로 들어오는 것을 의미.
        self.__company = company
        self.__inch = inch
        self.__price = price
        self.__color = color

    def __str__(self):
        print(f"제조사 : {self.get_company()}")
        print(f"인치 : {self.get_inch()}")
        print(f"가격 : {self.get_price()}")
        print(f"색상 : {self.get_color()}")

    #getter()
    def get_company(self):
        return self.__company
    def get_inch(self):
        return self.__inch
    def get_price(self):
        return self.__price
    def get_color(self):
        return self.__color

        
    #setter()
    def set_company(self, company):
        self.__company = company
    def set_inch(self, inch):
        self.__inch = inch
    def set_price(self, price):
        self.__price = price
    def set_color(self, color):
        self.__color = color
