'''

리스트 일치 검사를 하는 실습.
리스트가 일치하는 연산을 위해서 반드시 2개의 리스트가 반드시 동일한 자료형이어야 한다(중요)

'''

from posixpath import split


li1 = [10, 20, 30]
li2 = [10, 20, 30]
print(li1 == li2)

#== 연산자는 2개의 리스트가 길이가 서로 다르면 무조건 False이다.
li1 = [10, 20, 30]
li2 = [10, 20]
print(li1 == li2)

li3 = [4, 5, 2]
li4 = [4, 5, 0]
print(li3 > li4)

#아래 리스트는 >,<를 비교할 때 아스키코드를 가지고 비교한다.
li5 = ["a", "b", "c"]
li6 = ["a", "b", "d"]
print(li5 > li6)

#문자 -> 아스키코드 ord()
print(ord("c"))
print(ord("d"))
#아스키코드 -> 문자 char()
print(chr(99))
print(chr(100))

#리스트 정렬하기
#정렬하는 두가지 방법

#1번째 방법 : 리스트 객체의 sort() 메서드를 이용. 원본 리스트의 값이 변경이 된다.
li = [80, 90, 100, -70, -50]
a = li.sort() #리턴값이 없다.
print(li)
print(a)

#2번째 방법 : 내장함수로 존재하는 sorted() 메소드를 이용하는 방법, 원본 리스트는 유지, 정렬된 리스트를 반환.
li = [80, 90, 100, -70, -50]
a = sorted(li)
print(li)
print(a)

print("=" * 40)
#리스트 객체의 reverse()는 내림차순이 아니라 리스트 요소를 뒤집는 메서드
li = [80, 90, 100, -70, -50]
li.reverse()
print(li)

#reverse 매개변수의 값을 True로 설정하면 내림차순 정렬이 이루어진다.
print("=" * 40)
li = [80, 90, 100, -70, -50]
li.sort(reverse=True)
print(li)

#sorted()의 내림차순 정렬 방법
print("=" * 40)
li = [80, 90, 100, -70, -50]
a = sorted(li, reverse=True)
print(a)

#문자열을 정렬하기(유니코드를 기준으로 정렬을 한다.)
print("=" * 40)
li = ["하와이", "폭포", "가나", "한국"]
li1 = sorted(li, key=str.lower)
print(li1)

# 긴 문자열을 분리하는 방법(split()) 매개변수 따로 안주면 defalut 공백으로 분리함.
statement = "나는 한국에서 살고 있는 송관동입니다. 만나서 반갑습니다."
li = statement.split()
print(li)










