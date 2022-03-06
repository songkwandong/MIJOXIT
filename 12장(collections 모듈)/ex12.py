'''

namedtuple 모듈은 튜플의 형태로 데이터를 구조화에 맞게끔
저장하는 자료구조.

'''

#일반적인 튜플의 경우
person1 = ("신은혁", 14, "남")
person2 = ("강은비", 17, "여")

for n in [person1, person2]:
    # %n 들어가면서 튜플의 값들을 각각의 형식지정자에 맞게끔 적용시킨다.
    print("%s은(는) %d세의 %s성입니다." %n)
#일반적인 튜플은 .(접근연산자) 사용을 하지못하고 인덱스로만 접근이 가능.

print("=" * 40)
#namedtuple인 경우
from collections import namedtuple

#Person 이라는 namedtuple을 정의하는 것
Person = namedtuple(typename="Person", field_names=('name age gender addr'))
P1 = Person(name="김연아", age=32, gender="여성", addr="대전")
P2 = Person(name="손연재", age=28, gender="여성", addr="서울")

for n in [P1, P2]:
    print("%s은(는) %d세의 %s성입니다. 거주지는 %s입니다. " %n)

# Person이라고 정의를 해놓았고, 그의 필드들이 3개가 존재하고 있기 때문에
# namedtuple은 .(접근연산자)를 이용할 수 있고, 인덱스로도 접근이 가능하다.
print(P1.name, P1.age, P1.gender, P1.addr)
print(P1[0], P1[1], P1[2], P1[3])
print(P2.name, P2.age, P2.gender, P1.addr)

print("=" * 40)
#namedtuple의 _make()메소드 : 기존에 생성된 namedtuple에 새로운 인스턴스를 생성해주는
#메소드, _make() 안의 매개변수로 들어가는 것은 시퀀스 자료형이여야 한다.

P3 = Person._make(("신은혁", 15, "남", "대구"))

for n in [P1, P2, P3]:
    print("%s은(는) %d세의 %s성입니다. 거주지는 %s입니다. " %n)

print("=" * 40)
#namedtuple에서는 인덱스를 통한 값변경은 되지 않지만, _replace() 메소드로
#값의 변경이 가능하다.
P1 = P1._replace(name = "강백호")
P2 = P2._replace(age = 100)
P3 = P3._replace(addr="달성군")

for n in [P1, P2, P3]:
    print("%s은(는) %d세의 %s성입니다. 거주지는 %s입니다. " %n)

# 생성되어진 Person이라는 namedtuple의 _fileds 로써 Person에 있는 필드명
# tuple() 형식으로 리턴을 해준다.
print(P1._fields)

# getattr()는 필드명으로 그 값을 출력할 때 사용한다.
print(getattr(P1, 'name'))
print(getattr(P2, 'name'))
print(getattr(P3, 'name'))

# **(double-star-operator)은 딕셔너리 자료구조를 namedtuple()
# 변환하여 반환한다.

print("=" * 40)
dic = {"name":"신은비", "age":15, "gender":"여", "addr":"대전"}
print(dic)
print(type(dic))

P4= Person(**dic)
print("%s은(는) %d세의 %s성입니다. 거주지는 %s입니다. " %P4)
print(P4)
print(type(P4))