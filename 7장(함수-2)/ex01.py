'''

값에 의한 호출(call by value), 값에 의한 전달(pass by value)
은 동일한 개념이다.

함수를 호출할 때 값이 복사가 되어진다.(중요!)
호출한 곳에 영향을 끼치지 않는다.

숫자,문자 객체는 변경될 수 없는 immutable object이다.

'''

def change(num):
    print(f"change()내의 연산전의 num의 값: {num}")
    print(f"change()내의 연산전의 num의 주소:{id(num)}")
    num = num + 10
    print(f"change()내의 연산후의 num의 값: {num}")
    print(f"change()내의 연산후의 num의 주소:{id(num)}")
    return num

#파이썬에서는 모든 값들이 객체로 이루어져 있다.
n1 = 100

#id() 함수는 매개변수 값으로 객체를 받아서 그 객체의 고유한 주소값을 반환해주는 함수.
print(f"호출 전 n의 주소:{id(n1)}")
print(f"호출 전 n의 값: {n1}")
x = change(n1)
print(f"호출 후 x의 주소:{id(x)}")
print(f"호출 후 x의 값: {x}")
print(f"호출 후 n의 주소:{id(n1)}")
print(f"호출 후 n의 값: {n1}")