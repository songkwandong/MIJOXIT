'''

리스트
여러개의 값을 모아서 하나의 변수에 저장할 수 가 있는 데이터 타입.
아주 유용!
[]안에 값을 저장.

리스트 길이 알고 싶을 때도 len()을 사용
리스트는 문자열과 달리 인덱스 사용하여 값 변경 가능
리스트는 정수, 문자열에 국한되지 않고 여러개 값 저장 가능.

'''

city = ["서울", "부산", "대구", "광주", "인천"]
print(city)
print(city[2])

def all_list_value_print(list):
    for i in range(0,len(city)):
        print(city[i])

all_list_value_print(city)
city[1] = "전주"
print("=" * 30)
all_list_value_print(city)

name = input("이름: ")
age = int(input("나이: "))
address = input("주소: ")
height = int(input("키: "))
weight = int(input("몸무게: "))

person = [name, age, address, height, weight]
print(person)





