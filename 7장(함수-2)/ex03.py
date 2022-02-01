'''

call by reference에 대한 실습
함수를 호출할 때, 실질적인 주소값이 넘어가서 호출한 곳에 영향을 끼치는 형태가 된다.

파이썬에서는 함수의 매개변수값이 전부 객체인데, list, dictionary와 같은 mutable object 즉, 변경 가능한 객체이므로 call by objective-reference라고 한다.

'''

def change(li):
    print("=" * 40)
    print(f"change() 함수 내의 연산전의 li의 값:{li}")
    print(f"change() 함수 내의 연산전의 li의 주소값:{id(li)}")
    li += [100, 200]
    print("=" * 40)
    print(f"change() 함수 내의 연산후의 li의 값:{li}")
    print(f"change() 함수 내의 연산후의 li의 주소값:{id(li)}")

list = [1, "안녕하세요", 1.11]
print("=" * 40)
print(f"change() 함수 호출전의 li의 값:{list}")
print(f"change() 함수 호출전의 li의 주소값:{id(list)}")
change(list)
print("=" * 40)
print(f"change() 함수 호출전의 li의 값:{list}")
print(f"change() 함수 호츌후의 li의 주소값:{id(list)}")