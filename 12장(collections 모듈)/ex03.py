'''

OrderedDict 모듈 이름 그대로 순서를 가지는 딕셔너리 객체이다.

원래, 딕셔너리는 순서를 보장하지 않는 객체이다.
일반적인 딕셔너리는 순서를 보장하지 않는게 원래의 딕셔너리.
왜냐하면 딕셔너리는 인덱스가 없기 때문이다.
파이썬의 버전이 3.6 이상이 됨으로 일반 딕셔너리가 입력된 순서대로
출력이 되고 있음.
하지만 파이썬 버전 2.x 에서는 순서가 중구난방으로 나온다.

'''
#일반적인 딕셔너리
print("=" * 40)
dict = {}
dict["a"] = 100
dict["b"] = 200
dict["c"] = 300
dict["d"] = 400
dict["e"] = 500
dict["f"] = 500
dict["g"] = 500
dict["h"] = 500
dict["i"] = 500
dict["j"] = 500
dict["k"] = 500

for k,v in dict.items():
    print(k,v)

#OrderedDict 는 딕셔너리의 순서, 동등성 비교를 개선한 모듈
from collections import OrderedDict

print("=" * 40)
dict = OrderedDict()
dict["a"] = 100
dict["b"] = 200
dict["c"] = 300
dict["d"] = 400
dict["e"] = 500
dict["f"] = 500
dict["g"] = 500
dict["h"] = 500
dict["i"] = 500
dict["j"] = 500
dict["k"] = 500

for k,v in dict.items():
    print(k,v)

