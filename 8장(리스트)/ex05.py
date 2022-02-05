'''

인덱싱 : 리스트에서 하나의 요소를 인덱스를 통하여 참조하는 것.

'''

li = ["안녕", "송관동", 10, 100, -10]
print(li[2])

#음수 인덱스는 뒤에서부터 계산한다. 시작값은 -1이다.
print(li[-2])
print(li[-2 + len(li)])

#슬라이싱(slicing) : 리스트 범위 안에서 범위를 지정하여 원하는 요소들을 선택하는 연산을 칭한다.
li1 = ["안녕", "송관동", 10, 100, -10, False, True]
print(f"li1의 주소값:{id(li1)}")

#인덱스의 값을 통해서 부분 리스트를 새로 만든다.
s_li1 = li1[2:6]
print(f"s_li1의 주소값:{id(s_li1)}")
print(f"s_li1 : {s_li1}")

#슬라이싱 연산을 할 때, 앞의 인덱스가 생략되면 0부터 시작함을 이해하자.
s_li2 = li1[:6]
print(f"s_li2의 주소값:{id(s_li2)}")
print(f"s_li2 : {s_li2}")

s_li3 = li1[1:]
print(f"s_li3 : {s_li3}")

#아래의 코드는 li1의 값을 전부 출력한다.
print(li1[:])

#슬라이싱을 통해 값을 변경하는 내용 실습
#변경시에는 리스트는 하나의 리스트를 가지고 변경하여 주소값의 변경은 없다.
words = ["a", "b", "c", "d", "e"]
print(words)
print(f"words의 주소값:{id(words)}")

words[1:4] = ["B", "C", "D"]
print(words)
print(f"words의 주소값:{id(words)}")

#아래코드는 요소들이 다 삭제가 된다. 주소도 새로 받아옴
words = []
print(words)
print(f"words의 주소값:{id(words)}")
#주소 유지하려면 아래와 같이 해야한다.
words[:] = []
print(words)
print(f"words의 주소값:{id(words)}")

