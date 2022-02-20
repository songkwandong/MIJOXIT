'''

set은 수학의 집합과 같은 개념이다.
세트의 특징 : 요소들의 중복을 허용하지 않는다. 순서를 유지하지않는다.
{...} 을 이용해서 세트를 만든다.

'''

# 세트는 입력순서와 동일하게 출력하지 아니한다.
set1 = {2,1,34,5,3}
print(set1)
set2 = {"안녕", "하이", "사람", "자동차"}
print(set2)

#아울러 세트는 시퀀스형 자료형이다 보니 함수를 사용할 수 있다.
print(len(set1))
print(len(set2))
#세트는 중복을 허용하지 않는 특징이 있으므로 중복된 값을 출력하지 않는다.
set3 = {1, 2, "안녕", "하이", "사람", "자동차", "안녕", "하이"}
print(set3)
print(len(set3))

#세트의 요소가 있는지 확인하는 방법
if "안녕" in set3:
    print("set3에는 '안녕'이란 단어가 존재합니다.")

#세트의 요소를 루프를 통하여 출력하는 방법
for value in set3:
    print(value, end=" ")

# 세트는 순서를 유지하기 않기 때문에 인덱싱과 슬라이싱이 되지 않는다.
# TypeError: 'set' object does not support item assignment
#set3[0] = 80

#비어있는 세트를 만드는 방법
set4 = set()

#세트에 값을 추가하기(add() 사용)
# 세트는 모든 요소들을 해싱기법을 이용하여 저장하고 관리한다.
# 그래서 해싱가능(hashable)하여야 한다.
# 해싱이란 각각의 객체에 식별할 수 있는 해쉬코드를 부여하여 객체를 테이블에 저장하는 것이다.
set4.add("봄")
set4.add("여름")
set4.add("가을")
set4.add("겨울")
print(set4)

#세트는 요소가 해싱이 가능하려면 해쉬코드를 가져야 한다. 그 값이 변경되면 안된다.
# 따라서 세트는 변경 가능한 항목을 가지면 안된다.
# 하여 아래와 같이 리스트를 요소로 가지지 못하고 에러를 발생시킨다.
# TypeError: unhashable type: 'list'
#set5 = {1.1,2,"자동차",[10,20]}
# 튜플을 값 변경이 이루어지지 않는 객체이므로 세트의 요소가 될 수 가 있다.
set5 = {1.1,2,"자동차",(10,20)}
print(set5)

#여러개의 요소를 추가하려면  update() 메서드를 이용.
set6 = set()
# 아래 update() 문자열"인간"을 문자로 나누어서 세트에 저장이된다.
set6.update("인간",[1,34,5,-10])
print(set6)
# 아래 update() 문자열"인간"을 문자로 나누지 아니하고 세트에 저장이된다.
set6.update(["인간",1,34,5,-10])
print(set6)

print("="*40)
#세트의 요소를 삭제를 하고자 할 때
#discard() 리턴값이 없다.
set6.discard("인간")
print(set6)

set6.remove(-10)
print(set6)

#이미 삭제된 값은 keyError를 발생시킨다.
#set6.remove(-10)

set6.clear()
print(set6)
print(len(set6))