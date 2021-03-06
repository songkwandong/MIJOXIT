'''

튜플(tuple)에 대한 실습
튜플의 특징 : 리스트에 반하여 변경이 불가능한 객체이다. 리스트에 비해서 속도가 빠르다.
튜플도 시퀀스의 일종이다.

+ * min() max() len() tuple() 연산과 내장함수가 사용가능하다.
리스트는 대괄호 [] 요소를 감싸지만, 튜플은 () 요소를 감싼다.

'''
colors = ("red", "blue", "yello")

print(colors)
print(type(colors))

numbers = (1,2,3,4,5)
print(numbers)
print(type(numbers))

#튜플도 리스트와 마찬가지로 여러가지 자료형을 섞어서 생성할 수 있다.
tuple1 = (1, 2.2, "hi")
print(tuple1)
print(type(tuple1))

#공백 튜플 만들기.
tuple2 = ()

#튜플은 한번 생성되어지면 더이상 추가, 삭제, 수정이 불가하다.
#하나의 값만을 가지는 튜플을 생성할 때는 반드시 요소 뒤에 ,(콤마)를 적어줘야 한다.
#그렇지 아니하면 그냥 일반 정수나 문자열로 인식한다.
tuple3 = (10)
print(tuple3)
print(type(tuple3))

#리스트를 내장함수인 tuple()로 tuple로 만들수가 있다.
li =[1,2,3,4,5]
tuple4 = tuple(li)
print(tuple4)
print(type(tuple4))

#튜플도 리스트와 마찬가지로 내장 튜플을 가질 수 있다.

print("=" * 40)
t1 = (1, 2.2, "반가워요")
t2 = (3.3,4.4,5.5)
t3 = t1, t2
print(f"t1의 주소 : {id(t1)}")
print(f"t2의 주소 : {id(t2)}")
print(f"t3의 주소 : {id(t3)}")
print(f"t3[0]의 주소 : {id(t3[0])}")
print(f"t3[1]의 주소 : {id(t3[1])}")
print(t3)
print(type(t3))

#튜플도 시퀀스의 일종이므로 아래와 같이 내장함수 사용이 가능하다.
t4 = (1,2.2,3,"안녕")
t5 = (1, 2.2, 3)
print(f"t4의 길이: {len(t4)}")
#서로 다른 데이터 타입이 튜플의 요소로 존재한다면 비교가 되질 않는다.
print(f"t5의 가장 큰 값: {max(t5)}")
print(f"t5의 가장 작은 값: {min(t5)}")
t6 = (1, 2.2, 3, "안녕")
t7 = (1, 2.2, 3)
t8 = t6 + t7 #튜플은 + 연산이 가능하다(접합)
print(t8)

t9 = t7 * 2 # 튜플은 * 연산도 가능하다(반복)
print(t9)


if 2.2 in t6: #존재 여부를 알아봄.
    print("t6에는 2.2가 존재합니다.")
# 튜플은 시퀀스의 일종이니 반복문도 가능하다.
for x in t6:
    print(x, end=" ")
print()

#인덱싱
t10 = (1, 2.2, 3, "안녕", "철수", 5.5)
print(t10[4])
print(t10[-1])
print(t10[1:])

#슬라이싱
print(t10[4:6])
print(t10[-3:-1])

#dir() 함수는 객체가 사용할 수 있는 함수들을 출력해주는 역할을 하는 함수이다.
t1 = (1, 2.2, 3)
t2 = (1, 2.2, 3.7)
#print(dir(t1))
#튜플을 비교를 하고자 한다면, __eq__()를 사용하도록 하자.
print(t1.__eq__(t2))