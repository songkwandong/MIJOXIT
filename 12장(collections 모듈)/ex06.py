'''

함수를 이용하여 딕셔너리를 초기화 하는 코드를 실습

'''

from collections import defaultdict

# 일반 딕셔너리
def count_letters(words):
    counter = {}
    #넘어온 문자열의 문자하나가 키가 되고 그 키의 기본값을 0으로 설정
    for letter in words:
        if letter not in counter:
            counter[letter] = 0
    return counter

# setdefault() 메소드를 이용
def count_letters_setdefault(words):
    counter = {}
    #위의 함수보다 조건절 사라졌지만 루프를 돌 때마다, setdefault()를 계속 호출하므로
    #비효율
    for letter in words:
        counter.setdefault(letter, 0)
    return counter

# defaultdict 모듈을 직접 이용하는 방법.
def count_letters_defaultdict(words):
    counter = defaultdict(lambda : 0)
    for letter in words:
        counter[letter] += 1
    return counter


if __name__ == "__main__":
    dict1 = count_letters("가나다라마")
    print(dict1.items())
    
    dict2 = count_letters_setdefault("가나다라마")
    print(dict2.items())

    dict3 = count_letters_defaultdict("가나다라마")
    print(dict3.items())
    


