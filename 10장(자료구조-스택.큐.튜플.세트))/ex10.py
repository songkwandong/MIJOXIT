'''

부분 집합 연산

'''

SET1 = {10,20,30}
SET2 = {10,20,30}

#2개의 세트가 같은지를 검사하는 방법(==, !=)
print(f"SET1과 SET2가 같은가? : {SET1==SET2}")
print(f"SET1과 SET2가 다른가? : {SET1!=SET2}")

SET1 = {10,20,30,40,50,60}
SET2 = {10,20,30}

#부등호 연산을 이용하여 부분집합인지 아닌지를 알 수 있다.

#부분 집합 : SET2 집합이 SET1 집합에 포함시 SET2집합은 SET1 집합의 부분집합.
#상위 집합 : 위의 상황에서 SET1이 상위 집합.
#진상위 집합 : SET1 집합이 SET2 집합의 상위 집합이지만, 동일하지는 않음. 
#진부분 집합 : SET2 집합이 SET1 집합에 포함되지만 서로 집합은 동일하지않음

#연산자를 이용한 방법
print(f"SET2는 SET1에 부분집합인가? : {SET1>SET2}")
#issubset()을 이용한 방법
print(f"SET2는 SET1에 부분집합인가? : {SET2.issubset(SET1)}")

#상위 집합인지 확인하는 방법
#부등호로서는 확인할 수 있는 방법은 없다.
#print(f"SET1은 SET2에 상위집합인가? : {SET1<SET2}")
#issuperset()을 이용하는 방법
print(f"SET1은 SET2에 상위집합인가? : {SET1.issuperset(SET2)}")

#데이터 값이 집합에 포함되어있는지 확인하는 방법.
SET_STRING = set("안녕하세요")
print(SET_STRING)

if "안" in SET_STRING:
    print("'안' 문자는 SET_STRING 세트에 포함되어 있습니다.")

# 집합 연산을 할 수 있는 것이 set 자료구조의 장점.
# 합집합 : 연산자 | (파이프), union() 메서드를 이용

SET1 = {10,20,30,40,50,60}
SET2 = {10,20,30}

print("=" * 40)
print(f"합집합 : {SET1 | SET2}")
print(f"합집합 : {SET1.union(SET2)}")

#교집합은 두개의 집합에서 겹치는 요소를 구하는 연산.
#방법: 연산자 &, intersection() 이용.
print(f"교집합 : {SET1 & SET2}")
print(f"교집합 : {SET1.intersection(SET2)}")
print(f"교집합 : {SET2.intersection(SET1)}")

#차집합은 하나의 집합에서 다른 집합의 요소를 빼고 남은 집합.
#방법 : 연산자 - 를 사용하고나, difference()를 사용한다.
print(f"차집합 : {SET1 - SET2}")
print(f"차집합 : {SET1.difference(SET2)}")
print(f"차집합 : {SET2.difference(SET1)}")

#all() 집합에서 모든 값이 참이어야지만 참을 리턴.
#any() 집합에서 값이 하나라도 참이라면 참을 리턴.
SET1 = {10,20,30,40,50,60}
SET2 = {0,0,0,0,0,-7}
print(f"all()결과 : {all(SET1)}")
print(f"any()결과 : {any(SET2)}")

#집합이 첨부터 아예 다른지를 확인하고 싶을때(같은 요소가 없다.)
print(f"같은 요소가 없는가? :{SET1.isdisjoint(SET2)}")

#pop()로 집합의 요소를 제거할 수 있는데, 순서가 없기 때문에 임의로 아무요소나 삭제되게 된다.
#단 정수의 경우는 한번 가져올때의 패턴을 재실행해도 똑같지만 , 문자열 타입은
#삭제 및 출력 패턴이 실행될 때 마다 달라지는 것을 알 수가 있다.
for _ in range(0, len(SET1)):
    print(SET1.pop(), end=" ")
print()
print(len(SET1))

SET1={"한국","가나","일본","미국","영국"}
for _ in range(0, len(SET1)):
    print(SET1.pop(), end=" ")
print()
print(len(SET1))