'''

문자열의 중앙에 있는 문자를 추출해서 출력을 하는 프로그램을 만들기
예를 들어서 문자열이 "weekday"라면 중앙의 문자는 k
문자열이 짝수개의 문자라면 중앙에 문자 2개를 출력.
ex) monday =  nd
'''
input_str = input("문자열을 입력하세요 :")

input_str_len = len(input_str)
print_idx = input_str_len // 2
changed_input_str=""

if input_str_len % 2 == 0 :
    changed_input_str = input_str[(print_idx - 1) : (print_idx + 1)]
else:
    changed_input_str = input_str[print_idx]

print("출력 문자는 : {}".format(changed_input_str))