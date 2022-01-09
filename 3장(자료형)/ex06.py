'''

문자열의 인덱싱
인덱싱이란 문자열에서 문자를 추출하는데 문자열에는 각각에 해당하는 문자의 번호(인덱스)가 존재.
[인덱스] 하면 문자열에서 문자를 추출할 수가 있다.
인덱스라 함은 0부터 시작 즉, 마지막 인덱스는 n-1
파이썬 특수 기능 - 음수 사용 가능.

마지막 문자 구하기 - len(문자열)-1

문자열의 인덱스 범위 밖 값을 주면 index out of range 에러가 발생.

다른언어에 비해 파이썬은 문자열 인덱스로 문자열내 문자 치환이 불가능, 
즉, 한번 작성된 문자열은 변경이 불가능하다.

사용자로부터 문자열을 입력을 3개 받고, 각 해당 문자열의 첫 번째 문자를 인덱싱한 문자들을 합쳐서 문자열을 만드는 프로그램 작성

'''

word = "Python"
print(len(word))

for i in range(0,len(word)):
    print(word[i])

print(word[len(word)-1])
#print(word[100])

#word[2] = 'B'


def concat_string(n):
    input_cnt = n
    input_string=""
    concat_string=""

    for i in range(0, n):
        input_string = input("문자열을 입력해주세요.")
        print("남은 횟수 : {}".format(n-(i+1)))
        concat_string = concat_string + input_string[0]
    
    return concat_string
    
print(concat_string(3))