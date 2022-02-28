'''

딕셔너리의 항목들을 순회하는 방법

'''

scores = {"국어":80, "수학":95, "영어":80}

#키값만 출력되도록 루프를 돌게
#아래 print() 문을 이용하여 keys()를 사용하면 반환값의 형태가
#dict_keys([]) 타입으로 출력된다.
print(scores.keys())
print(type(scores.keys()))

#아래와 같이 루프를 돌리면 키값만 출력이 된다.
for subject in scores.keys():
    print(subject, end=" ")
print()
print("=" * 40)

#값만 출력하는 방법
#dict_values([]) 타입으로 출력된다.
print(scores.values())
print(type(scores.values()))
for value in scores.values():
    print(value, end=" ")

print()
print("=" * 40)
#아래와 같이 루프를 돌리면 키와 값을 동시에 출력한다.(튜플 형태)
print(scores.items())
print(type(scores.items()))
for i in scores.items():
    print(i, end=" ")

print()
print("=" * 40)
#딕셔너리 함축(dcitionary comprehension) 방법은 코드를 간결하게 만들고
#가독성도 좋아진다.

triples = { x:x*x*x for x in range(6)}
print(type(triples))
print(triples)

#딕셔너리 정렬(dcitionary sort) 방법 실습
#파이썬에서는 딕셔너리는 근본적으로 요소들이 순서가 없기 떄문에 순서대로 저장하지 않는다.
dic1 = {"pens":6, "bags":1, "books":5, "bottles":4, "coins":3, "cups":2}
print(dic1)

#딕셔너리를 리스트로 변환함 (키값만)
li1 = list(dic1)
print(li1) 

#딕셔너리의 키를 정렬하고자 한다면 내장함수 sorted() 메소드 사용.
li2 = sorted(dic1)
print(li2)

print("=" * 40)
#딕셔너리의 값을 정렬하고자 한다면 values() 함수와 sorted()를 같이 사용
li3 = sorted(dic1.values())
print(li3)

print("=" * 40)
#딕셔너리의 값에 따라서 키들을 정렬하고 싶은 경우 sorted()에 요소들을 비교할때
#사용하는 키를 지정.
print(sorted(dic1, key=dic1.__getitem__))