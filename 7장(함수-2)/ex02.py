'''

문자열 전달에 대한 실습
문자열에 대한 내용도 앞서 살펴본 숫자형의 객체와 동일한 변경될 수 없는 immutable object 형태이다.
파이썬의 경우는 타 언어의 call by value 개념과는 조금 다르다.
-> 파이썬은 모든 것을 "객체"로 판단하기 때문이다.

파이썬의 이런 특성이 존재하므로 call by objective라고도 칭한다.


'''

def change(string):
    print(f"change()내의 연산전의 string의 값: {string}")
    print(f"change()내의 연산전의 string의 주소:{id(string)}")
    string += "공부합니다."
    print(f"change()내의 연산후의 string의 값: {string}")
    print(f"change()내의 연산후의 string의 주소:{id(string)}")

msg = "안녕하세요 저는 파이썬을 "
print(f"호출 전 msg 값 : {msg}")
print(f"호출 전 msg 의 주소값 : {id(msg)}")
change(msg)
print(f"호출 후 msg 값 : {msg}")
print(f"호출 후 msg 의 주소값 : {id(msg)}")