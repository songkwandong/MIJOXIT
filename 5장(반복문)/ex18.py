'''

더블 루프를 사용하여 아래와 같이 출력하는 프로그램을 작성하시오.
출력결과

*
**
***
****
*****


'''
#1번째 방법(더블 루프)
for y in range(5):
    for x in range(y+1):
        print("*", end="")
    print("")

#2번째 방법(format() 함수 이용)
#format() 함수는 {}이용하고 숫자도 같이 이용된다.
#format 함수도 인덱스를 활용하여 해당하는 값들을 출력할 수가 있다.

for x in range(5):
    star='*'
    print(f"{star * (x + 1)}")


print("정수:{} String:{} Float:{}".format(10, "Hi ~", 10.1))
print("정수:{0} String:{1} Float:{2}".format(10, "Hi ~", 10.1))
print("정수:{2} String:{1} Float:{0}".format(10, "Hi ~", 10.1))

#format()는 공간확보 및 0으로 채우는 기능도 지원한다.
#콜론(:)을 기준으로 우측에 > 혹은 < 부등호를 사용해서 방향을 지정해줄 수 있다.
#0을 앞에 추가하면 빈칸을 0으로 채워줌.

print("숫자 '{:>05d}'".format(300)) #오른쪽(>)으로 밀어서 출력.
print("숫자 '{:<5d}'".format(300)) #왼쪽(<)으로 밀어서 출력.

for i in range(5):
    print("{0:<5}".format("*" * (i + 1)))

'''

*****
****
***
**
*

'''
#더블 루프
print("-" * 40)
for y in range(5):
    for x in range(5 - y):
        print("*", end="")
    print("")

print("-" * 40)
for i in range(5, 0, -1):
    print("{0:<5}".format("*" * (i)))