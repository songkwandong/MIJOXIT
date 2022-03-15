'''



'''

from Tv import *

if __name__ == "__main__":
    #인스턴스 생성
    tv1 = Tv()
    tv2 = Tv()

    #인스턴스의 필드와 메서드를 tv1 인스턴스명(참조변수) 조작
    tv1.color = "검정색"
    tv1.powerTv(True, "tv1")
    tv1.channel_up(9, "tv1")
    tv1.volume_up(25, "tv1")
    tv1.__str__("tv1")
    tv1.channel_up(-100, "tv1")
    tv1.powerTv(False, "tv1")
    tv1.volume_up(30, "tv1")

    print("=" * 40)
    tv2.color = "흰색"
    tv2.powerTv(True, "tv2")
    tv2.channel_up(17, "tv2")
    tv2.volume_up(50, "tv2")
    tv2.__str__("tv2")
    tv2.channel_up(-100, "tv2")
    tv2.powerTv(False, "tv2")
    tv2.volume_up(30, "tv2")