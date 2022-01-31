'''

모듈 형태로 되어 있는 함수들의 집합

간단한 함수
def 키워드 함수이름(매개변수)

def say_hello(name): #함수의 선언부(헤더)
    print(f"안녕하세요 {name}님") #함수의 구현부(정의부, 몸체)

함수를 정의만 하면 출력값은 없다. 출력값이 나오게 할려면 호출(call)을 해야한다.
함수 호출 (fuction call)

함수의 매개변수명이 name이니 웬만하면 이름을 매개변수 값으로 주는것이 현명한 코드.

'''

def say_hello_name(name):
    print(f"안녕하세요 {name}님") 

def say_hello_name_msg(name, msg):
    print(f"안녕하세요 {name}님 {msg}") 

def get_sum(start, end):
    hap = 0
    for i in range(start, end + 1):
        hap += i
    return hap