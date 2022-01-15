'''

논리 연산자(logical operator)는 두 개 이상의 조건을 조합해서 참인지 거짓인지를 계산할 때 사용하는 연산자이다.
논리 연산자의 종료 and(논리곱), or(논리합), not(논리부정)
0이 아닌 값은 참이다.

and 연산자는 여러개의 조건 중에서 처음 조건이 거짓이라면 뒤의 조건은 검사조차 하지않는다.(단축 계산)

and 연산자는 모든 조건이 참이여야만 참을 반환한다!
or 연산자는 모든 조건 중에서 하나만 참이면 참을 반환을 한다!
or 연산자는 모든 조건이 거짓이여야만 거짓을 반환을 한다!
not은 조건이 참이면 전체 조건식의 결과를 반대로 거짓으로 만들고
조건식의 결과가 거짓이라면 참으로 바꾸는 역할을 한다.

'''

#and
name = "송관동"
age = 14
height = 171

if (age == 14 ) and (height >= 170) and (name == "김관동"):
    print("{}님은 놀이 기구를 탈 수 있습니다.".format(name))
else:
    print("{}님은 놀이 기구를 탈 수 없습니다.".format(name))
    
#or
print("-" * 40)

if (age == 15 ) or (height >= 180) or (name == "김관동"):
    print("{}님은 놀이 기구를 탈 수 있습니다.".format(name))
else:
    print("{}님은 놀이 기구를 탈 수 없습니다.".format(name))

#not
print("-" * 40)

if not (1 == 1):
    print("참 입니다.")
else:
    print("거짓입니다.")


