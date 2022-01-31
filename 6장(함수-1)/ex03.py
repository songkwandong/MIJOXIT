'''

두 개의 정수를 입력받아서 두 수 중에서 더 큰 수를 찾아서 리턴하는 함수 

함수의 목록이 정의되어 있는 모듈을 import 할 때는 항상 개발코드의 상위에 위치할 수 있도록 해야 한다.

'''

import calc

# left = int(input("비교할 값 1을 입력하세요:"))
# right = int(input("비교할 값 2를 입력하세요:"))
# print(f"입력 1값은 : {left}, 2값은 {right}, max값은 :{calc.get_max(left, right)}입니다.")


# left = int(input("비교할 값 1을 입력하세요:"))
# right = int(input("비교할 값 2를 입력하세요:"))
# print(f"입력 1값은 : {left}, 2값은 {right}, min값은 :{calc.get_min(left, right)}입니다.")

left = int(input("거듭 제곱 할 수를 입력하세요:"))
right = int(input("거듭 제곱의 횟수를 입력하세요:"))
print(f"거듭 제곱 할 값은 : {left}, 거듭 제곱의 횟수 값은 {right}, min값은 :{calc.get_power(left, right)}입니다.")


