'''

학생들의 성적을 처리하는 프로그램을 만들기.
조건 : 사용자로부터 성적을 입력을 받아서 리스트에 저장한다.
성적의 평균을 구하고 해당 점수가 80점 이상 성적을 받은 학생의 수를 출력       

학생수는 상수값으로 STUDENT=5를 이용한다.
'''


def input_score(student_cnt : int) -> list:
    score_list = []
    
    for i in range(student_cnt):
        score = int(input("성적을 입력하시오:"))
        score_list.append(score)
    
    return score_list

def cal_score_avg(score_list: list) -> int: 
    sum = 0
    for i in range(len(score_list)):
        sum += score_list[i]
    return round((sum / len(score_list)), 1)

def check_over_score_student_cnt(score_list: list) -> int:
    cnt = 0
    for i in range(len(score_list)):
        if score_list[i] >= 80:
            cnt += 1
    return cnt

def main():
    score_list = input_score(STUDENT_CNT)
    
    score_avg = cal_score_avg(score_list)
    print(f"성적 평균은 {score_avg} 입니다.")
    
    over_score_student_cnt = check_over_score_student_cnt(score_list)
    print(f"80점 이상 성적을 받은 학생은 {over_score_student_cnt} 입니다.")

    
if __name__ == "__main__":
    STUDENT_CNT = 5
    main()
