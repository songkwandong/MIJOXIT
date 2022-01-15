'''

사용자로부터 태어난 연도를 입력받아서 초등학생, 중학생, 고등학생, 대학생 분류 중 어디에 해당하는지 
출력하는 프로그램.(현재 나이)
나이 : 8~13(초등학생), 14~16(중학생), 17~19(고등학생) 20~27(대학생), 이외의 나이라면 일반인으로 분류.

'''

current_year = 2022

birth_year = int(input("태어난 연도 입력해주세요.:"))
age = current_year - birth_year

if age < 8:
    print("응애")
elif age <= 13:
    print("초등학생 입니다.")
elif age <= 17:
    print("중학생 입니다.")
elif age <= 19:
    print("고등학생 입니다.")
elif age <= 27:
    print("대학생 입니다.")
else:
    print("일반인 입니다.")