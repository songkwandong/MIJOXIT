'''

한 사람이 돈이 5000원 있는데 사탕 가격이 120원이라면 최대로 살 수 있는 사탕의 수를 출력하는 프로그램

'''

myMoney = 5000
candyPrice = 120

#/ = 실수 // = 정수로 결과가 나옴 
maxBuyCandieNum = myMoney // candyPrice

print("최대로 살 수 있는 사탕의 개수: {}".format(maxBuyCandieNum))

change = myMoney % candyPrice

print("잔돈: {}".format(change))