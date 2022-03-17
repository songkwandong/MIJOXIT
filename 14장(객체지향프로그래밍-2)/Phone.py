'''
Phone 클래스 정의(조상클래스)
모든 클래스의 최고 조상클래스는 object 클래스이다.


'''

class Phone(object):
    #멤버의 개수는 8개
    #생성자
    def __init__(self) -> None:
        self.model = ""
        self.color = ""

    #메서드 정의
    def power_on(self):
        print("전원을 켭니다.")
    
    def power_off(self):
        print("전원을 끕니다.")
    
    def bell(self):
        print("벨이 울립니다.")
    
    def send_voice(self, message):
        print(f"자신 : {message}")
    
    def receive_voice(self, message):
        print(f"상대방 : {message}")

    def hang_up(self):
        print("전화를 끊습니다.")
    