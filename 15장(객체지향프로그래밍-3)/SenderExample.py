'''

ContentSender, KakaoSender, SmsSender 클래스의 실행 파일.

'''

from KakaoSender import *
from SmsSender import *

if __name__ == "__main__":
    cs1 = KakaoSender("카카오톡", "이재훈", "100만원 갚아라")
    cs1.send_msg("빚쟁이 이재훈")

    print("=" * 40)

    cs2 = SmsSender("SMS 문자", "신은혁", "고마워 은혁아")
    cs2.send_msg("멋쟁이 신은혁")
    