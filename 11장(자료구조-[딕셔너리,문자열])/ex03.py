'''

영한 사전 만들기
공백 딕셔너리 생성하고 여기에 영어단어를 키로 하고 설명을 값으로 저장
출력결과
단어를 입력하시오. : one
하나
단어를 입력하시오. : python
해당하는 단어가 없습니다.
종료하려면 종료

'''

younghan_dict = dict()

younghan_dict["one"] = "하나, 일"
younghan_dict["two"] = "둘, 이"
younghan_dict["three"] = "셋, 삼"
younghan_dict["four"] = "넷, 사"
younghan_dict["five"] = "다섯, 오"

while True:
    word = input("단어를 입력하시오. (종료 입력시 종료):")
    if word == "종료":
        break
    elif word in younghan_dict.keys():
        print(younghan_dict[word])
    else:
        print("해당하는 단어가 없습니다.")


