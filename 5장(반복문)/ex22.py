'''

사용자로부터 문자열을 입력받아서 알파벳 문자의 개수, 숫자의 개수, 스페이스의 개수를 출력하는 프로그램 작성.
(isalpha는 한글도 지원한다.)
'''

s = input("문자열을 입력하세요.:")

alpha_cnt = 0
digit_cnt = 0
spaces = 0

for ch in s:
    if ch.isalpha():
        alpha_cnt += 1
    elif ch.isdigit():
        digit_cnt += 1
    elif ch.isspace():
        spaces += 1
    else:
        print("알파벳도, 숫자도, 공백도 아닙니다.")

print(f"알파벳 개수:{alpha_cnt}, 숫자 개수:{digit_cnt}, 공백 개수:{spaces}")
