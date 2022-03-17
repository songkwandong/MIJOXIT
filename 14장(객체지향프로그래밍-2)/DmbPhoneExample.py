'''

Phone 클래스와 DmbPhone 클래스를 이용하여 
메인코드 작성

'''

from DmbPhone import *

if __name__ == "__main__":
    #자손클래스의 인스턴스 생성.
    dmb_phone = DmbPhone("파이썬폰", "검정색", 10)

    #조상클래스에게 상속받은 필드.
    print(f"모델 : {dmb_phone.model}")
    print(f"색상 : {dmb_phone.color}")
    #자손클래스 필드.
    print(f"채널 : {dmb_phone.channel}")

    dmb_phone.power_on()
    dmb_phone.bell()
    dmb_phone.send_voice("여보세요")
    dmb_phone.receive_voice("안녕하세요! 저는 송관동입니다.")
    dmb_phone.send_voice("아 안녕하세요 반갑습니다.")
    dmb_phone.hang_up()

    #자손클래스에서 만든 dmb 기능
    print("=" * 40)
    dmb_phone.turn_on_dmb()
    dmb_phone.change_channel(15)
    dmb_phone.turn_off_dmb()
    dmb_phone.power_off()