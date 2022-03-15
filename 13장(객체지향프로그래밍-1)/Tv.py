'''

클래스 Tv를 설계하는 코드


'''


class Tv:
    #필드를 선언
    color = ""    #색상
    power = False #전원
    channel = 0   #채널
    volume = 0    #볼륨

    #Tv를 전원을 켜거나 끄는 멤버 메서드
    def powerTv(self, power, tv):
        self.power = power
        if self.power == True:
            print(f"{tv}의 전원이 켜졌습니다.")
        else:
            print(f"{tv}의 전원이 꺼졌습니다.")

    #Tv의 채널을 올리는 기능을 하는 멤버 메서드
    def channel_up(self, channel, tv):
        if channel < 0:
            print("채널은 음수일 수 없습니다.")
            return
        if self.power == False:
            print(f"{tv}의 전원 부터 켜주세요.")
            return
        else:
            self.channel += channel
    
    def channel_down(self, channel, tv):
        if channel < 0:
            print("채널은 음수일 수 없습니다.")
            return
        if self.power == False:
            print(f"{tv}의 전원 부터 켜주세요.")
            return
        else:
            self.channel -= channel
    
    def volume_up(self, volume, tv):
        if volume < 0:
            print("볼륨은 음수일 수 없습니다.")
            return
        if self.power == False:
            print(f"{tv}의 전원 부터 켜주세요.")
            return
        else:
            self.volume += volume

    def volume_down(self, volume, tv):
        if volume < 0:
            print("볼륨은 음수일 수 없습니다.")
            return
        if self.power == False:
            print(f"{tv}의 전원 부터 켜주세요.")
            return
        else:
            self.volume -= volume
    
    #__str__() 인스턴스의 멤버 변수들의 값을 찍어보는 용도로 사용된다.
    def __str__(self, tv):
        print(f"{tv}의 색상 : {self.color}")
        print(f"{tv}의 채널 : {self.channel}")
        print(f"{tv}의 볼륨 : {self.volume}")