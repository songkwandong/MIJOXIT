'''

grade 모듈 만들기

'''

#아래 함수는 사용자로부터 성적을 입력받는다.
#사용자가 음수를 입력하면 성적 입력받는 것을 멈추도록한다.
def read_list() -> list:
    score_list = []
    flag = True

    while flag:
        score = int(input("성적을 입력하세요(종료를 하시려면 음수를 입력):"))
        if score >= 0:
            score_list.append(score)
        else:
            print("종료하겠습니다.")
            flag = False

    return score_list

#입력받은 성적의 오름차순 정렬하는 함수
def sorting_list(score_list: list) -> list:
    score_list.sort()
    return score_list
    
#오름차순 정렬이 된 성적을 출력하는 함수.
def show_score(score_list: list) -> None:
    cnt = 0
    for i in score_list:
        print(f"{cnt + 1}번째 성적: {i}")
        cnt += 1        