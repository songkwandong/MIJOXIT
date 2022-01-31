'''

함수(function)에 대한 실습

1. 함수는 프로그램안에서 중복된 코드를 제거한다.
2. 복잡한 프로그래밍 작업을 더 간단한 작업들로 분해할 수 있다.
3. 함수는 한번 만들어두면 재사용이 얼마든지 가능하다.
4. 함수를 사용하면 가독성이 증대되고, 유지관리도 쉬워진다.

'''
#hello.py 파일의 내용을 전부 다 가져오기 때문에 파일명.함수명으로 접근 하지않아도 되고 함수명만 호출하면 된다. 
#from hello import *

#파일명.함수명으로 접근해야한다.
import hello

my_name = "송관동"
hello.say_hello_name(my_name)
my_name = "홍길동"
hello.say_hello_name(my_name)

name = "송관동"
msg = "만나서 반갑습니다."
hello.say_hello_name_msg(name, msg)

name = "홍길동"
msg = "도와주세요."
hello.say_hello_name_msg(name, msg)

# 파이썬에서는 오버로딩의 개념이 없다. 같은 함수의 이름이라면 마지막에 정의되어진 함수만 인식하게 된다.
# 함수명은 유니크한 값으로 함수명을 짓도록 한다.


#값을 반환하는 함수 예제

result = hello.get_sum(1,10)
print(type(result))
print(f"1~10까지의 누적합 :{result}")

result = hello.get_sum(1,30)
print(f"1~30까지의 누적합 :{result}")

result = hello.get_sum(1,100)
print(f"1~100까지의 누적합 :{result}")