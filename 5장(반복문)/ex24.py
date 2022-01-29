'''

입력받은 문자열의 모든 공백을 제거한 문자열을 출력하는 프로그램을 작성.


'''

statements = input("원하는 문자열을 입력하세요.")
result = ""

for ch in statements:
    if ch != " ":
        result += ch

print(f"입력한 문자열은 : {statements}")
print(f"공백을 제거한 문자열은 : {result}")