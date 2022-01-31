'''

사용자로부터 정수를 입력받아서 소수를 판별하는 함수 is_prime()을 작성해보자.
소수이면 True, 아니면 False를 출력하도록.

'''

num = int(input("정수를 입력하세요 : "))
def is_prime(num):
    is_prime_flag = False
    is_prime_check = 0

    for i in range(2, num + 1):
        if num % i == 0:   
            is_prime_check = i   
            break
    if num == is_prime_check or num == 1:
        is_prime_flag = True
    print(is_prime_flag) 

is_prime(num)
    
    