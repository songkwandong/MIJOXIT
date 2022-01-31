'''

키워드 인수(keyword argument)

통상 프로그래밍 언어라면 함수의 매개변수의 위치를 기준으로 해서 
해당 인수를 매칭을 해줌으로써 함수의 값이 전달(복사)가 된다.

이것을 다른말로 위치 인수 방식(positional argument)이라고 한다.

'''

def calc(x, y, z):
    print(f"x: {x}")
    print(f"y: {y}")
    print(f"z: {z}")
    return x + y + z

#통상적으로 calc()를 호출시에는 위치 인수 방식
print(calc(1, 2, 3))

#키워드 인수 형태로 호출하는 방법
#장점: 매개변수의 위치에 얽메이지 않고 직접 키워드값에 할당함으로서 함수 호출이 이루어진다.
print(calc(y=1, z=2, x=3))


