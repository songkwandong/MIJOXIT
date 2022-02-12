'''

탐색하기 
주어진 데이터 내에서 어떠한 특정한 값을 찾는 행위가 탐색하는 것이다.
index()를 이용하여 일반적인 탐색이 가능.

'''

# word_list = ["gold", "blue", "red", "yellow", "green"]
# search_word = input("찾고자 하는 단어를 입력해주세요.:")

# if search_word in word_list:
#     index = word_list.index(search_word)
#     print(f"찾고자 하는 단어가 {index}에 존재합니다.")
# else:
#     print("찾고자 하는 단어가 없습니다.")

#프로그래머가 직접 탐색을 하는 알고리즘을 구현해야 하는 경우도 상당히 많음,
#탐색의 가장 기본적인 방법이 순차 탐색
#순차 탐색은 리스트의 요소를 순서대로 하나씩 꺼내서 탐색키 값과 비교해서 성공하면
#루프를 빠져나오고 루프를 다했음에도 없다면 탐색키가 존재하지 않음을 의미.

def number_search(list: list, key: int) -> None:
    cnt = 0
    for i in range(len(list)):
        if key == list[i]:
            cnt += 1 
    return cnt

num_list = []
for i in range(10, 110, 10):
    num_list += [i]

num_list += [50]
num_list += [50]
num_list += [50]
num_list += [50]

key = int(input("찾고자하는 정수를 입력해주세요."))
cnt = number_search(num_list, key)

if cnt == 0:
    print(f"{key}는 존재하지않습니다.")
else: 
    print(f"{key}는 {cnt}개 존재합니다.")

#모든 조건에 만족하는 항목을 전부 찾는 방법
result = []
for i in num_list:
    if i >= key:
        result.append(i)

print(result)

#바로 위에 있는 코드를 사용자로부터 키를 입력받아서 키값 이상의 값들을 출력하고 
#그 키값 이상인 값들의 총 갯수를 구하는 프로그램을 작성해보시오.
print(len(result))