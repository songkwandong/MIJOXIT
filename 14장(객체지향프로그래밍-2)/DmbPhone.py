'''

Phone 클래스의 자손클래스인 DmbPhone 클래스 정의


'''

from Phone import *

class DmbPhone(Phone):
    #멤버의 개수가 12개
    #생성자
    def __init__(self, model, color, channel) -> None:
        #조상클래스 생성자 호출 2가지 방법
        #자손클래스 생성자 구현부의 첫 줄에 적어주는걸 권장.
        super().__init__()
        #Phone.__init__(self)

        self.model = model
        self.color = color
        self.channel = channel

    #메서드 추가
    def turn_on_dmb(self):
        print(f"채널 :{self.channel}번 DMB 방송 수신을 시작합니다.")
        
    def turn_off_dmb(self):
        print("DMB 방송 수신을 종료합니다.")
    
    def change_channel(self, channel):
        self.channel = channel
        print(f"채널 :{self.channel}번으로 채널을 변경합니다.")


