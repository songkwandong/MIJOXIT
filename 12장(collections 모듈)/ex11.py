'''

Counter 모듈의 메서드 실습

'''

from collections import Counter

count = Counter()
print(count)

#update() : Counter의 값을 갱신하는 것을 의미
count.update("안녕하세요.")
print(count)

count.update({"안":3, "요":5, "가":3})
print(list(count.elements()))

#most_common(n) 입력된 값의 요소들 중에서 빈도수가 높은 순으로 상위 n개를 리스트안에
#튜플 형태로 반환하는 메서드

print("=" * 40)
count = Counter("apple, orange, grape")

# 매개변수를 주지 않았을 때는 전체 문자열을 대상으로 값과 빈도수를 출력
# 매개변수를 주었을 때는 전체 문자열을 대상으로 빈도수 순서가 높은 순 n개만큼 출력
print(count.most_common())
print(count.most_common(3))

#substract() : 단어 그대로 요소의 값을 빼는 것을 의미.
#요소가 없는 경우에는 음수의 값을 출력한다.

print("=" * 40)
c1 = Counter("반갑습니다. 안녕하세요.")
c2 = Counter("반갑다.친구야")

c1.subtract(c2)
print(c1)

print("=" * 40)
# Counter() 는 산술/집합 연산이 가능.
# 덧셈
c1 = Counter(["a", "b", "c", "d", "e"])
c2 = Counter("apple")

print(c1)
print(c2)
print(c1 + c2)

print("=" * 40)
# 연산자로 뺄셈을 하면 음수의 값은 출력하지 않음.
# substract와의 차이점

c1.subtract(c2)
print(c1)
c1 = Counter(["a", "b", "c", "d", "e"])
print(c1 - c2)

print("=" * 40)
# Counter 모듈의 교집합 및 합집합 출력하는 기능
c1 = Counter("abcdefg")
c1 = Counter("abcd가나다라")

#교집합 & 연산자
print(f"교집합 :{c1 & c2}")

#합집합 | 연산자
print(f"합집합 :{c1 | c2}")

print("=" * 40)
#덧셈과 뺄셈만 Counter 모듈은 허용, *, /, % 연산자는 지원하지 않는다. 