'''

bool 변수 알아보기
타 프로그래밍 언어에서는 부울 변수의 값은 소문자로 시작하는데 반해, true, false
파이썬은 True, False를 사용함을 잊지 말자.

부울 변수의 값을 바꾸기 위해선 not 연산자를 앞에 두면 논리 부정의 값으로 변환된다.

'''

flag = True

print(type(flag))
#<class 'bool'>
print(flag)
#True

if flag:
    print("True라서 실행 됩니다.")
else:
    print("False라서 실행 됩니다.")
    
flag = not flag

print(flag)
#Flase

if flag:
    print("True라서 실행 됩니다.")
else:
    print("False라서 실행 됩니다.")
    