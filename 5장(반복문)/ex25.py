'''

입력받은 문자열을 거꾸로 출력하는 프로그램을 작성

'''

statements = input("문자열을 입력하세요:")

reverse_statements = ""

for ch in statements:
    reverse_statements = ch + reverse_statements

print(f"입력한 문자열은 : {statements}")
print(f"역순으로 출력한 문자열은 : {reverse_statements}")

print("-" * 40)

s_list = list(statements)
#reverse()는 리스트 타입을 역순으로 바꿔주는 함수,
s_list.reverse()
#join() 함수는 역순으로 된 문자열을 연결해서 출력해주는 함수
print("".join(s_list))

#reversed()는 문자열에만 역순으로 하는 함수.
print("-" * 40)
print("".join(reversed(statements)))

#파이썬에서는 [::-1]을 사용해서 문자열을 역순으로 출력할 수 있다.
print("-" * 40)
print(statements[::-1])

#문자열 3번째 인덱스부터 역순으로 출력하는 방법.
print("-" * 40)
print(statements[3::-1])