'''

사용자로부터 상품금액을 입력받아서 상품의 총 가격을 계산하는 프로그램 만들기
사용자가 몇개의 상품을 살지 모르니깐 무한루프를 이용하고 아울러 사용자가 "끝"이라고 입력을 하면 루프를 탈출.

클래스 -> 객체
클래스의 구성요소

1. 멤버 변수
2. 멤버 함수(메서드)
3. 생성자

'''

#from operator import eq
import operator

total = 0 

# while True:
#     price = int(input("상품 금액을 입력해주세요:"))
#     total += price
#     end_flag = input("입력을 그만두시겠습니까? (아니오 / 끝) :")
    
#     if end_flag == "끝":
#         print(f"상품 금액의 총 가격은 {total}입니다.")
#         break

price = ""

while True:
    price = input("상품 금액을 입력하세요. (끝을 입력하면 종료):")
    if operator.eq(price, "끝"):
        print(f"상품 금액의 총 가격은 {total}입니다.")
        break
    total += int(price)
    
