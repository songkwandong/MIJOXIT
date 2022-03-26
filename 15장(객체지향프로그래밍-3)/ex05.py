#다형성 실습

class Product: 
    price = 0 
    bonus_point = 0

    #매개변수가 있는 생성자
    def __init__(self, price) -> None:
        self.price = price
        #보너스 점수는 제품 가격의 10프로를 적립함.
        self.bonus_point = int(self.price / 10.0) 

class Tv(Product):
    def __init__(self, price) -> None:
        #조상클래스의 생성자 호출
        super().__init__(price)

    # 무엇을 구매를 했는지 확인하기 위해 __str__ 재정의
    def __str__(self) -> str:
        return "TV"

class Computer(Product):
    def __init__(self, price) -> None:
        #조상클래스의 생성자 호출
        super().__init__(price)

    # 무엇을 구매를 했는지 확인하기 위해 __str__ 재정의
    def __str__(self) -> str:
        return "COMPUTER"

class Audio(Product):
    def __init__(self, price) -> None:
        #조상클래스의 생성자 호출
        super().__init__(price)

    # 무엇을 구매를 했는지 확인하기 위해 __str__ 재정의
    def __str__(self) -> str:
        return "AUDIO"

#물건을 사는 독립적 클래스
class Buyer:
    money = 1000
    bonus_point = 0
    #매개변수의 다형성을 이용
    def buy(self, product):
        #가진 돈보다 제품의 가격이 비싼 경우
        if self.money < product.price:
            print("잔액이 부족하여 물건 구입이 안됩니다.")
            return
        #가진 돈에서 구입한 제품의 가격을 빼준다.
        self.money -= product.price
        #제품의 보너스 점수를 추가.
        self.bonus_point += product.bonus_point
        print(product.__str__() + "를 구매하셨습니다.")
    
    def __str__(self) -> str:
        print(f"현재 잔액: {self.money} 만원")
        print(f"현재 보너스 포인트: {self.bonus_point} 만원")
        


if __name__ == "__main__":
    buyer = Buyer()
    tv = Tv(300)
    computer = Computer(100)
    audio = Audio(50)
    #생성된 인스턴스를 Buyer클래스의 buy()메서드의 매개변수 값으로 대입하고 있다.

    buyer.buy(tv)
    buyer.__str__()

    buyer.buy(computer)
    buyer.__str__()

    buyer.buy(audio)
    buyer.__str__()

    buyer.buy(Tv(300))
    buyer.__str__()

    buyer.buy(Computer(100))
    buyer.__str__()

    buyer.buy(Tv(500))
    buyer.__str__()




















