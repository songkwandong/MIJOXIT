'''

성적 처리 프로그램 만들기(2차원 리스트를 이용)
주어진 성적
score = [
    [100,100,100],
    [20,20,20],
    [30,30,30]
    [40,40,40]
    [50,50,50]
]

출력 결과
번호    국어    영어    수학    총점    평균
------------------------------------------
1
2
3
4
5
------------------------------------------

총점 

'''

score = [
    [100,100,100],
    [20,20,20],
    [30,30,30],
    [40,40,40],
    [50,50,50]
]


def print_list(li : list)->None:
    korea_total = 0
    english_total = 0
    math_total = 0
    sum_total_score = 0
    total_avg = 0.0

    for i in range(len(li)):
        total_score = 0
        avg_score = 0.0
        
        #각 과목별 점수 누적
        korea_total += li[i][0]
        english_total += li[i][1]
        math_total += li[i][2]

        print(f"{i + 1}", end="\t")
        for j in range(len(li[i])):
            total_score += li[i][j]
            print(f"{li[i][j]}", end="\t")

        sum_total_score += total_score
        avg_score = total_score // len(li[i]) 
        total_avg += avg_score
        print(f"{total_score}\t{avg_score}")

    total_avg //= len(li)
    print("-" * 45)
    print(f"총점\t{korea_total}\t{english_total}\t{math_total}\t{sum_total_score}\t{total_avg}")

print("번호\t국어\t영어\t수학\t총점\t평균")
print("-" * 45)
print_list(score)
