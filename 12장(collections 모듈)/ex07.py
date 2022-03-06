'''

함수를 이용하여 각 알파벳의 글자의 수를 세어서 키로 저장하고 글자가 값인 딕셔너리를 리턴
(list이용)
'''

from collections import defaultdict

# words라는 리스트를 받아서 길이를 키로 하고 값을 리스트 값으로 하는 딕셔너리 리턴
def counter_words(words):
    grouper = defaultdict(list)
    
    for word in words:
        #word의 길이를 구하여 그 길이를 키로 하고 word의 내용을 값으로
        length = len(word)
        grouper[length].append(word)
    return grouper

if __name__ == "__main__":
    li1 = ["감자", "귤", "사과", "배", "오징어", "꼼장어", "불가사리"]
    
    dic1 = counter_words(li1)
    print(dic1)
    print(dic1[2])
    