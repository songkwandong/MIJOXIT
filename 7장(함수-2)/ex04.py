'''

mutable object중 dictionary 라는 타입이 있다.
딕셔너리라는 타입의 형태는 키와 값의 쌍으로 이루어져있다.
{key:value} 로 이루어져 있으며, 키값은 유니크한 값으로 변경 불가, value 값은 변경이 가능하다.
딕셔너리의 call by reference 가 성립되는 이유는 변경 가능한 mutable object이기 때문에 가능한 것이다.
call by objective-reference라고도 칭한다.

'''

def change(dic):
    print("=" * 40)
    print(f"change() 함수 내의 연산전의 dic의 값:{dic}")
    print(f"change() 함수 내의 연산전의 dic의 주소값:{id(dic)}")
    dic["몸무게"] = 42
    print("=" * 40)
    print(f"change() 함수 내의 연산후의 dic의 값:{dic}")
    print(f"change() 함수 내의 연산후의 dic의 주소값:{id(dic)}")


dict = {"name":"송관동", "age":29, "height":187}
print(dict)
#키를 주고 값을 얻어온다.
print(dict["name"])
print("=" * 40)
print(f"change() 함수 호출전의 dic의 값:{dict}")
print(f"change() 함수 호출전의 dic의 주소값:{id(dict)}")
change(dict)
print("=" * 40)
print(f"change() 함수 호출전의 dic의 값:{dict}")
print(f"change() 함수 호츌후의 dic의 주소값:{id(dict)}")


