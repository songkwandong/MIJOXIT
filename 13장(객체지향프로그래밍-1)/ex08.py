'''

클래스 변수와 인스턴스 변수의 다른 예제

'''


class Card:
    kind = ""
    number = 0

    #클래스 변수
    width = 100 
    height = 250

    def __init__(self, kind, number):
        self.kind = kind
        self.number = number
    
    def __str__(self):
        print(f"kind : {self.kind}")
        print(f"number : {self.number}")
        print(f"width : {Card.width}")
        print(f"height : {Card.height}")


if __name__ == "__main__":
    card1 = Card("다이아몬드", 10)
    card1.__str__()

    card2 = Card("스페이드", 11)
    card2.__str__()