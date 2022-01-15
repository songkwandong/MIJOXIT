'''

몸무게와 키를 입력받고 BMI가 20.0 이상이고, 25.0미만이면 표준,
아니면 체중관리가 필요합니다. 라고 출력해주는 프로그램


BMI = 몸무게 / ((키/100.0)^2) / 
'''



height = float(input("키를 입력해주세요.(단위 cm) :"))
height /= 100.0

weight = float(input("키를입력해주세요.(단위 kg) :"))
bmi_value = (weight / (height ** 2)) 

print("BMI는 {}입니다.".format(bmi_value))
if (bmi_value >= 20.0) and (bmi_value < 25.0):
    print("표준입니다~")
else: 
    print("체중 관리가 필요합니다~")