'''

자동 판매기를 시뮬레이션하는 프로그램을 작성, 사용자는 1000원권 지폐와 500원,100원 짜리 동전을 사용할 수가 있다.
물건값을 사용자로부터 입력을 받아서 1000원권 지폐, 500원,100원짜리 동전의 개수를 입력하면 거스름돈을 계산해서 반환하는 프로그램

'''

item_price = int(input("물건값을 입력하세요:"))
bill_1000_cnt = int(input("1000원 지폐 개수 입력:"))
coin_500_cnt = int(input("500원 동전 개수 입력:"))
coin_100_cnt = int(input("100원 동전 개수 입력:"))
 
nod_money =((bill_1000_cnt * 1000) + (coin_500_cnt * 500) + (coin_100_cnt * 100)) - item_price
print("\n거스름돈은 : {}".format(nod_money))

def cal_change_coin_cnt(nod_money, coin_value):
    coin_change_cnt = nod_money // coin_value
    print("{}원짜리 동전 개수는 : {}".format(coin_value,coin_change_cnt))
    nod_money = nod_money % coin_value
    return nod_money

nod_money = cal_change_coin_cnt(nod_money, 500)
nod_money = cal_change_coin_cnt(nod_money, 100)
nod_money = cal_change_coin_cnt(nod_money, 50)
nod_money = cal_change_coin_cnt(nod_money, 1)




