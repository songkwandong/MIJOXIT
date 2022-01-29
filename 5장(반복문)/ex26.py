'''

왼쪽 공백만 제거하는 함수
lstrip()

오른쪽 공백만 제거하는 함수
rstrip()

양쪽 공백을 제거하는 함수.
strip()

이렇게 해도 중간에 공백은 사라지지않음.
-> for문 if문으로 공백 지울 수 있음.

'''

statements = "     안녕!"
print(f"공백 제거 전: {statements}")
print(f"왼쪽 공백 제거: {statements.lstrip()}")

print("-" * 40)
statements = "안녕!     "
print(f"공백 제거 전: {statements}")
print(f"오른쪽 공백 제거: {statements.rstrip()}")

print("-" * 40)
statements = "      안녕!     "
print(f"공백 제거 전: {statements}")
print(f"오른쪽 공백 제거: {statements.strip()}")


print("-" * 40)
statements = "      안      녕!     "
print(f"공백 제거 전: {statements}")
print(f"오른쪽 공백 제거: {statements.strip()}")

#문자열 나누기
print("-" * 40)
statements = "나는 열심히 파이썬 공부를 합니다."
print(statements.split())

for i in statements.split():
    print(i)


