'''
은행 계좌에 돈을 저금할 수 있고, 인출을 할 수도 있다.
은행 계좌를 간단하게 클래스로 정의해보자.

은행계좌(Account)는 현재 잔액(balance)을 필드로 
선언하고 기본 생성자를 작성하고, 

입금(deposit)메소드와
출금(withdraw)메소드 작성.

출력결과
통장에 1,000,000원이 입금됨.
현재잔액 : 1,000,000원
통장에 200,000원이 출금됨
현재잔액: 800,000원

'''

class Account:
    __balance = 0

    def __init__(self):
        pass

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    def deposit(self, money):
        self.set_balance(self.get_balance() + money)
        print(f"통장에 {money:,}원이 입금됨")
        self.__str__()

    def withdraw(self, money):
        self.set_balance(self.get_balance() - money)
        print(f"통장에 {money:,}원이 출금됨")
        self.__str__()
    
    def __str__(self):
        print(f"현재 잔액 : {self.get_balance():,}원")
        

if __name__ == "__main__":
    account1 = Account()
    account1.deposit(1000000)
    account1.withdraw(200000)