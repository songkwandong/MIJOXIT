'''

Counter 모듈은 시퀀스 자료형의 데이터의 값의 개수를 딕셔너리 형태로 반환.
같은 값이 몇개가 존재하는지 쉽게 알아보고자 할 때 사용하면 편리


'''

from collections import Counter

text = list("high school")

print(text)
print(type(text))

#Counter 객체를 만드는데 인자값으로 리스트형을 줌.
count = Counter(text)
print(count)
print(type(count))

#시퀀스 자료형에서 어떤 문자의 개수를 알고 싶을때도 사용 가능
print(count["h"])


print("=" * 40)
#Counter() 객체를 만들때, 값=개수 와 같은 형태로 입력도 가능.
count = Counter(A=3, b=1, c=5, a=3)
print(count)

#elements() 는 Counter로 주어진 값의 요소에 해당하는 값을 풀어서 반환
#요소는 무작위적으로 반환하며 요소의 수가 1보다 작을 경우
#출력하지 않는다. 대소문자를 구별하며 sorted() 정렬이 되어진다.
print(sorted(count.elements()))

print("=" * 40)
#a = "가"
#b = "나"
#count = Counter(a=3, b=5)

# 값=개수 형태로 Counter() 객체를 만들 때는 문자열은 매개변수로 쓸 수가 없다.
# 문자열 자체를 매개변수로 넣어주는 것은 아래와 같이 가능하다.
count = Counter("가나다라마바사")
print(count)
print(sorted(count.elements()))

#아래 문자열은 소문자로 바뀌고, 단어별로 만들어진 리스트가 반환
text = "abcdedfg abcdedfg repeat count! you can do it nice to meet yo. A count" \
    "telephone!!!".lower().split()
print(text)
print(Counter(text))

print("=" * 40)
count = Counter({"가":4, "나":3})
print(count)
print(list(count.elements()))