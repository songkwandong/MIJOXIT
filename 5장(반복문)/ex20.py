'''

소수를 2부터 계속 더할 때 2000까지 루프를 돌리고, 소수와 합계, 마지막으로 더해지는 소수는 얼마인지 출력하는 프로그램을 작성.
더블루프, 조건식 사용.

'''

start_num = 0
num = 0
sum = 0
last_data = 0

for num in range(2, 2001): 
    for start_num in range(2, num + 1):
        if num % start_num == 0:
            break
    if num == start_num:
        print("소수 :{0}".format(start_num))
        sum += start_num
        print("합계 :{0}".format(sum))
        last_data = start_num
        print("마지막 소수의 값 :{0}".format(last_data))

print(f"최대합은 {sum}, 마지막 더해지는 소수는{last_data}입니다.")