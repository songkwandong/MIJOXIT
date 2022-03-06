'''

defaultdict 모듈은 딕셔너리의 요소를 생성할 때, 키에 기본값을 지정하는 방법

일반적인 딕셔너리를 생성하고, 키의값으로 값을 알아낼 수 가 있다.
'''

dict1 = dict()
print(dict1)
#빈 딕셔너리에 "a"라는 키가 없다는 오류 발생.
#print(dict1["a"])
print(dict1.get("a"))

from collections import defaultdict

#defaultdict의 아직 모르는 모든 키에대해서 기본값을 0으로 지정.
dict1 = defaultdict(lambda : 0) #lambda를 이용하여 0을 리턴
print(dict1["a"])
print(dict1["b"])
print(dict1[100])
print(dict1)

print("=" * 40)
dict1 = defaultdict(int) # 키에 대한 값을 int형으로 설정
#dict1 = defaultdict(float) # 키에 대한 값을 float형으로 설정
#dict1 = defaultdict(str) # 키에 대한 값을 str형으로 설정
dict1["a"] += 100 #해당 키에 대한 값에다가 연산을 할 수도 있다.
print(dict1["a"])
print(dict1["b"])
print(dict1[100])
print(dict1)

