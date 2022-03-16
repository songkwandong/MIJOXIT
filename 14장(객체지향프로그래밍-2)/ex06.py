'''

None 참조값 : 변수가 아무것도 가리키고 있지 않다면 None으로 초기화를
해주는 것이 권장사항이다.

모든 변수는 초기화를 해주는 것이 제일 좋다.
None(C언어, 자바에서는 null)은 아무것도 참조하지 않고 있다는 특별한 값.

'''

class TV:
    # power = False
    # volume = 0
    # channel = 0

    def __init__(self, power, channel, volume) -> None:
        self.power = power
        self.channel = channel
        self.volume = volume

    def change_power(self):
        self.power = not self.power

    def __str__(self) -> str:
        print(self.power)
        print(self.volume)
        print(self.channel)

if __name__ == "__main__":
    tv = None
    print(tv) #결과가 None이 나오는 것이 당연, 인스턴스를 생성하지 않았기 때문
    print("=" * 40) 

    #AttributeError TV가 없는데 어떻게 power()를 호출할 수 있는가.
    #tv.change_power()
    tv = TV(True, 10, 25)
    tv.__str__()
    tv.change_power()
    print("=" * 40)
    tv.__str__()
    