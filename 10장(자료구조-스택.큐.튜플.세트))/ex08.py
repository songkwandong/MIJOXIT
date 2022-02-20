'''

data_list = [(90,80), (85,75), (90,100)] 튜플을 원소로하는 
리스트를 활용하여 학생의 총점과 평균(소수 첫째자리)을 출력하는 프로그램을 작성.

enumerate() 함수를 이용한다.
1번 학생의 총점은 170점이고, 평균은 85.0입니다.

'''


#enumerate() 함수의 역할: 반복문 사용시 몇 번째 반복을 확인할 때 사용을 한다.
if __name__=="__main__":
    data_list = [(90,80), (85,75), (90,100)]
    for idx, scores in enumerate(data_list):
        total_point =0 
        for score in scores: 
            total_point += score 
        
        print(
            f"{idx + 1}번 학생의 총점은 {total_point}이고, " \
            f"평균은 {total_point/len(scores):.2f} 입니다.")