'''

튜플 대입 연산에 대한 실습
튜플 패킹(packing) : 튜플에다가 값을 저장
튜플 언패킹(packing) : 튜플에서 값을 추출해서 변수에 대입하는 과정 

'''

#값을 교환할 떄 : 일반적 방법
x = 10
y = 20
temp = 0 #빈컵의 역할
print(f"값 변경 전(x, y): {x},{y}")
temp = x
x = y
y = temp
print(f"값 변경 후(x, y): {x},{y}")
print("=" * 40)

#값을 교환할 때 : 튜플 이용하는 방법

(a, b) = 100, 200
print(f"값 변경 전(a, b)): {(a, b)}")
(c, d) = (b, a)
print(f"값 변경 후(c, d): {(c, d)}")
# 인자값들이 서로 맞게끔 줘야 된다.
# 그렇지 아니하면 not enough values to unpack ValueError 가 발생.
# (x,y,z) = (10,20)

# 여러개의 변수를 한번에 할당하는 방법

person = ("신은혁", 14, "중학생")
(name, age, student_grade) = person

print(f"name : {name}, age: {age}, student_grade : {student_grade}")