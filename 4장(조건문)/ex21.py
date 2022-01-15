'''

학점을 세부적으로 나누는 프로그램을 작성하기(중첩 if문 사용)
조건 
1. 사용자로부터 정수를 입력받는다.
2. 정수가 95이상 100이하라면 A+을 출력한다.
3. 90이상 94이하라면 A0를 출력한다.
다른 B, C, D도 학점도 위와 같이 출력한다.

단 F는 그냥 출력하도록 한다.

'''

grade_point = int(input("학점을 입력하세요:"))
grade = ""

if grade_point >= 90:
    if grade_point >= 95:
        grade = "A+"
    else:
        grade = "A0"
elif grade_point >= 80:
    if grade_point >= 85:
        grade = "B+"
    else:
        grade = "B0"
elif grade_point >= 70:
    if grade_point >= 75:
        grade = "C+"
    else:
        grade = "C0"
elif grade_point >= 60:
    if grade_point >= 65:
        grade = "D+"
    else:
        grade = "D0"
else:
    grade = "F"

print("당신의 점수는 {}이며, 학점은 {}입니다.".format(grade_point, grade))
