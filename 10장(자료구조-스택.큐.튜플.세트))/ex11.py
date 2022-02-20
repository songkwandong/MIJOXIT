'''

아래와 같이 두개의 세트가 있다.
두개의 세트에 있는 사람 이름 중에 

2개의 파티에 모두 참석한 사람은 누구인가를 출력.

partyA에 속하는 사람은 "신은혁", "김연아", "손연재", "김철수"
partyB에 속하는 사람은 "최양락", "김기훈", "손연재", "안철수"

출력결과
2개의 파티에 모두 참석한 사람은 아래와 같습니다.

'''

def get_intersection_person(partyA:set, partyB:set)->set:
    return partyA & partyB
        


partyA = set(["신은혁", "김연아", "손연재", "김철수"])
partyB = set(["최양락", "김기훈", "손연재", "안철수"])

print("2개의 파티에 모두 참석한 사람은 아래와 같습니다.")
intersection_person = get_intersection_person(partyA, partyB)
print(f"{intersection_person}")