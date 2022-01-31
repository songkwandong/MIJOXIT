'''

함수가 리턴값이 없는 경우에 대한 예제

'''

def printInfo(name, age):
    print("=" * 40)
    print(f"이름 : {name}")
    print(f"나이 : {age}")
    print("=" * 40)

    #리턴값이 존재하지 않는다면 return문 뒤에 아무 값도 적어주지 않는다.
    return 

print("이름과 나이를 입력해주세요. :")
end_input = "y"

while True:
    if end_input == "n":
        print("입력을 종료합니다.")
        break
    elif end_input == "y":
        name = input("회원명을 입력해주세요:")
        age = int(input("나이를 입력해주세요:"))
        printInfo(name, age)

    end_input = input("입력을 종료하시겠습니까? (y or n):")

