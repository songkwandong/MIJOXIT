'''

쇼핑몰에서 물건을 구매할 때, 구입액이 5만원 이상이면 5%의 할인을 해준다.
사용자에게 구입 금액을 입력 받고, 최종적으로 얼마를 내야하는지 출력하는 프로그램 

''' 

DISCOUNT_PERCENT=0.05

total_price = int(input("할인 전 금액을 입력하세요(단위 = 원): "))

if total_price >= 50000 :
    discount_price = total_price * DISCOUNT_PERCENT
    total_price = total_price - discount_price
else:
    print("할인 금액 대상이 되질 않습니다.")

print("지불해야할 최종 금액은 {}입니다.".format(round(total_price)))