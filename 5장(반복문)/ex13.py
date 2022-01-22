'''

사용자로부터 임의의 개수의 성적을 입력받아서 합계와 평균을 계산한 후 출력하는 프로그램을 작성해보시오
단, 센티널은 음수의 값을 사용하시오.


'''

cnt = 0
avg = 0
hap = 0
score = 0

#센티널(보초값)을 사용자에 제시하는 코드
print("종료하려면 음수를 입력하세요. (예 : -1)")

while score >= 0 :
    score = int(input("{}번째 학생의 성적을 입력해주세요.".format(cnt + 1)))
    if score < 0 :
        break
    hap += score
    cnt += 1

if cnt > 0 :
    avg = hap / cnt
print(f'합계는 {hap}, 평균은 {avg:.1f} 입니다.')

