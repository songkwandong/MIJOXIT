'''

항공사에서는 짐을 부칠 때, 20kg이 넘어가면 20,000원의 추가비용을 내야한다고 하자.
20KG 미만이면 수수료는 없다. 사용자로부터 짐의 무게를 입력 받고 사용자가 지불해야하는 금액이 얼마인지 계산하는 프로그램을 작성해보자.

'''

baggage_weight = int(input("짐의 무게를 입력해주세여(단위 : kg) : "))
additional_cost = 0

if baggage_weight > 20:
    additional_cost = 20000
    print("내야 할 금액은 {}원 입니다.".format(additional_cost))
else:
    print("내야 할 금액은 {}원 입니다.".format(additional_cost))

print("감사합니다. 고갱님")