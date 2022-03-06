'''

일반 딕셔너리를 정렬을 하여 OrderedDict로 포장하기

'''
#일반적인 딕셔너리
print("=" * 40)
dict = {}
dict["z"] = 100
dict["a"] = 200
dict["e"] = 300
dict["d"] = 400
dict["h"] = 500
dict["j"] = 500
dict["g"] = 500
dict["k"] = 500
dict["1"] = 500
dict["3"] = 500
dict["m"] = 500

#키, 값으로 정렬
li1 = sorted(dict.keys())
li2 = sorted(dict.values())
print(li1)
print(li2)
print(dict["3"])

from collections import OrderedDict

#넘어오는 t의 값은 딕셔너리의 요소
#하여 0인덱스는 키값이 될 것이다.

def sort_by_key(t):
    return t[0]
    #return t[1]

print("=" * 40)
dict1 = {}
dict1["z"] = 100
dict1["a"] = 200
dict1["e"] = 300
dict1["d"] = 400

# li3 = sorted(dict1.items(), key=sort_by_key)
# print(li3)

#일반 딕셔너리의 내용을 sorted() 를 이용하여 정렬을 하면 키를 기준으로 정렬된 리스트가 리턴.
#OrderedDict()로 포장(wrapping)을 하고 있다.
#기존의 딕셔너리나 리스트의 순서를 지키면서 딕셔너리의 형태로 관리할 수가 있다.

for k, v in OrderedDict(sorted(dict1.items(), key=sort_by_key)).items():
    print(k,v)


#딕셔너리의 동등성 비교
# 동등성은 논리적 동등이라는 것을 의미한다. 논리적 동등이란 주소는 다르지만
# 요소들의 값의 순서가 비록 틀리더라도 논리적 동등으로 바라보는 시점이다.
# 일반적인 딕셔너리의 동등성 비교

dic1= {"가":1, "나":2, "다":3}
dic2= {"가":1, "다":3, "나":2}

print(id(dic1))
print(id(dic2))

print(dic1 == dic2)

#OrderedDict는 두개의 OrderedDict를 비교할 때 해당하는 값들의
#순서와 해당하는 키와 값이 같아야지만 동등하게 바라봄.
#일반적인 딕셔너리보다 좀 더 깐깐하고 디테일하게 비교하는 것이
#OrderedDict의 특징이다.

print("=" * 40)
ordered_dic1 = OrderedDict({"가":1, "나":2, "다":3})
ordered_dic2 = OrderedDict({"가":1, "다":3, "나":2})

print(id(ordered_dic1))
print(id(ordered_dic2))

print(ordered_dic1 == ordered_dic2)

#결론.
#OrderedDict 모듈은 딕셔너리의 순서대로 저장하지 않는 방식을 순서대로
#저장하는 방식으로 개선되었다.(파이썬 버전이 3.6이후로는 저장과 출력이 OrderedDict와 동일하게
# 작동하고있지만 2.x 버전에서는 문제점이 발생)
#
#딕셔너리의 동등성 비교에서 일반적인 딕셔너리는 순서를 유지하지 않아도 해당 키와 값이
#동등하다면 True를 리턴하지만 OrderedDict에서는 순서, 키, 값이 무조건 같아야
#Ture를 리턴하는 좀 더 깐깐한 동등성 비교로 개선되었다.
#OrderedDict를 사용하면 정확한 데이터의 순서나 값을 유지하는데 일반 딕셔너리에
#비해서 좋다.
#웬만하면 딕셔너리보다는 OrderedDict 모듈을 이용.

