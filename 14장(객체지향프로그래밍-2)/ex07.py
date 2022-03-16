'''

클래스 안의 상수를 많이 사용한다.
상수는 보통 클래스변수 형태로 지정하여 사용한다.

'''

class Character:
    #상수값 정의
    WEAK = 0
    NORMAL = 10
    STRONG = 20
    VERY_STRONG = 30

    def __init__(self) -> None:
        self.__hp = Character.NORMAL
    
    def level_up(self):
        self.__hp = Character.STRONG
    
    def damage(self):
        self.__hp = Character.WEAK

    def __str__(self) -> str:
        return f"HP : {self.__hp}"

if __name__ == "__main__":
    ch = Character()
    print(ch)

    ch.level_up()
    print(ch)

    ch.damage()
    print(ch)