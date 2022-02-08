'''

일반적인 리스트 연산들 실습
최소값 초대값을 구하는 알고리즘

'''

#내장함수를 이용하여 최소값 최대값을 구하는 코드
num = [1, 5, -9, 100]

print(f"최소값: {min(num)}")
print(f"최대값: {max(num)}")

#최대값과 최소값을 구하는 알고리즘은 상당히 중요한 개념.

prices = [1000, 3000, 500, 10000, 20000, 700]
#먼저 prices[]에 있는 0번째 인덱스 값을 변수에 저장

low_price = prices[0]
high_price = prices[0]

#이후 루프를 돌면서 조건식으로 값이 작으면 해당하는 값을 low_price 변수에 재저장.
for i in range(1, len(prices)):
    if low_price > prices[i]:
        low_price = prices[i]
print(f"가장 저렴한 가격은:{low_price}")

for i in range(1, len(prices)):
    if high_price < prices[i]:
        high_price = prices[i]
print(f"가장 비싼 가격은:{high_price}")

print("-" * 40)
#min, max()의 경우 문자열의 맨앞의 아스키 값부터 비교한다.
words = ["dog", "cat", "horse", "lion", "tiger", "elephant", "cat"]
words_han = ["안녕", "하이", "가지마세요" "반갑습니다", "가세요", "오랜만입니다"]
print(f"가장 짧은 단어 :{min(words)}")
print(f"가장 긴 단어 :{max(words)}")
print(f"가장 짧은 단어 :{min(words_han)}")
print(f"가장 긴 단어 :{max(words_han)}")

#문자열에서 가장 짧은 문자열을 구하는 알고리즘 코드
shortest_word = words[0]
shortest_list_word = []

for i in range(1, len(words)):
    if len(shortest_word) >= len(words[i]):
        if len(shortest_word) > len(words[i]):
            shortest_list_word.clear()
            shortest_list_word.append(words[i])
            shortest_word = words[i]
        else:
            shortest_list_word.append(words[i])
        
        
print(f"가장 짧은 단어는:{shortest_list_word}")

#문자열에서 가장 긴 문자열을 구하는 알고리즘 코드
longest_word = words[0]
for i in range(1, len(words)):
    if len(longest_word) < len(words[i]):
        longest_word = words[i]

print(f"가장 긴 단어는:{longest_word}")
