'''

문자열의 연결
number -> string str()함수 사용하여 타입 변경 가능.

문자열의 반복
문자열 * n n번만큼 반복.

%s (형식 지정자)
형식을 지정해서 상황에 맞게끔 출력하도록.

복수개를 사용하고자 하면, "%s %s %s" %(1,2,3) 각 매칭 대입해주어야 한다.

'''

first_name = "Kwan Dong"
last_name = "Song "

full_name = last_name + first_name
print(full_name)

temp = "Person" + str(100)
print(temp)


temp = "Person" + str(100.188)
print(temp)

price = int("123456")
print(type(price), price)

price = float("123456.1234")
print(type(price), price)

arrow= "==> \t" * 10
print(arrow)

price = 1000
print("가격 : %s" % price)

time = "13:49"
print("현재 시간 : %s" % time)

temp = "현재 시간은 %s시 %s분 %s초 입니다."
print(temp % (10,20,30))

