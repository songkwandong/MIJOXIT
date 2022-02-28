'''

회문이란 것은 앞으로 읽으나 뒤로 읽으나 동일한 문장을 의미.
ex ) "mom", "civic", "dad" 

사용자로부터 문자열을 입력받고 회문인지 아닌지 검사하는 프로그램 작성. 


'''


def main():
    input_str = input("문자열을 입력하시오.:")
    input_str = input_str.replace(" ","")

    if check(input_str) == True:
        print("회문입니다.")
    else:
        print("회문이 아닙니다.")


def check(string: str) -> bool:
    low = 0
    high = len(string) - 1
    while True:
        #계속 비교하여 아래의 조건이 된다면, 회문
        if low > high:
            return True
        s1 = string[low]
        s2 = string[high]
        print(s1,s2)
        #값이 틀리므로 회문이 아니다.
        if s1 != s2:
            return False
        #인덱스를 증가시켜서 서로 비교항목을 바꾸도록 한다.
        low += 1
        high -= 1



if __name__ == "__main__":
    main()
    # if input_str == input_str[::-1]:
    #     print("회문입니다.")
    # else:
    #     print("회문이 아닙니다.")