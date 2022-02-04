'''
지역변수(local variable)와 전역변수(global variable)에 대한 실습
지역변수 : 파이썬에서는 함수 안에 정의된 변수를 지역변수라고 하며, 지역변수가 범위(scope)는
함수 내에서만 사용이 되고 함수가 호출이되고 종료가 되면 지역변수는 소멸된다.

'''

# def test():
#     text = "파이썬 공부" # 지역변수 text에 문자열 할당.
#     print(text)         # 출력함수를 이용하여 text를 출력함.

# #test()를 호출한 후, "파이썬 공부"라는 문자열을 출력하면서 리턴값은 없다.
# test()


def test():
    text = "파이썬 공부" 
    print(text)         

test()
#아래 출력함수에서 에러 발생, 함수내에서 text 변수 생성, 소멸되어 text 변수가 정의되지 않았기 때문
# print(text)