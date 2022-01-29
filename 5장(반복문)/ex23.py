'''

사용자로부터 전화번호를 입력받다 보면 "-"를 적는 경우가 많다.
"-"를 합하여 입력받도록 하고, 출력을 할 때는 "-" 삭제를 한 문자열을 출력하는 프로그램 작성.


'''

call_num = input("전화번호를 입력하세요:")
new_call_num = ""

# 010-111-1111 or 010-1111-1111
if len(call_num) == 12 or len(call_num) == 13:
    for ch in call_num:
        if ch !="-":
            new_call_num += ch
else:
    print("전화번호 입력이 잘못되었습니다.")
    
print(new_call_num)