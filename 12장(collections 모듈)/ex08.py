'''

함수를 이용하여 각 알파벳의 글자의 수를 세어서 키로 저장하고 단어가 값인 딕셔너리를 리턴
(set 이용)

'''

from collections import defaultdict

# words라는 set을 받아서 길이를 키로 하고 값을 리스트 값으로 하는 딕셔너리 리턴
def counter_words(words):
    grouper = defaultdict(set)
    
    for word in words:
        #word의 길이를 구하여 그 길이를 키로 하고 word의 내용을 값으로
        length = len(word)
        grouper[length].add(word)
    return grouper

if __name__ == "__main__":
    set1 = set()
    set1.add("한국")
    set1.add("미국")
    set1.add("우즈베키스탄")
    set1.add("사우디아라비아")
    set1.add("스페인")
    
    dic1 = counter_words(set1)
    print(dic1)
    