'''

defaultdict의 초기값을 리스트 형태로 만드는 실습


'''

from collections import defaultdict

li1 = [("yellow", 1),("bule", 2),("green", 3),("bule", 4),("red", 1)]
dic1 = defaultdict(list)

for k, v in li1:
    dic1[k].append(v)

print(dic1)