'''

Monitor 클래스를 이용한 실습

'''

from Monitor import *

if __name__ == "__main__":
    #매개변수가 있는 생성자를 호출하는 방법
    # company, inch, price, color
    monitor1 = Monitor("LG", 32, 300000, "흰색")
    monitor1.__str__()
    print("=" * 40)

    #아래와 같이 setter()를 통하여 기존에 생성자로 생성했던 값을 변경
    monitor1.set_company("삼성")
    monitor1.set_inch(27)
    monitor1.set_price(150000)
    monitor1.set_color("검정")
    monitor1.__str__()



    
