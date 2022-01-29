'''

반복문으로 문자열 관련 처리하기 실습

'''


fruit = "apple"

for letter in fruit:
    print(letter, end=" ")

#사용자로부터 문자열(영문)을 입력받아서 모음을 전부 없애는 코드.
print("")
print("-" * 40)

s = input("문자열을 입력하세요(영문자):")
vowels = "aeiouAEIOU"

for letter in s:
    if letter not in vowels:
        print(letter, end="")

print("")
print("-" * 40)
original = input("문자열을 입력하세요(영문자):")

# 입력 받은 문자열을 전부 소문자로 변경
word = original.lower()
# 대문자는 upper()

vowels = 0
consonant = 0

#문자열의 길이가 0 초과, 알파벳이라면 참을 반환
if len(original) > 0 and original.isalpha():
    for ch in word:
        # 루프변수의 값이 모음에 해당하면, 
        if ch in "aeiou":
            vowels += 1
        else:   #자음이라면
            consonant += 1

print(f"모음의 개수:{vowels}, 자음의 개수:{consonant}")
