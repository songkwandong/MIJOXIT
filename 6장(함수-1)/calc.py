
#제곱을 구하는 함수
def squared(num):
    return num ** 2

    
#return 문은 최소화하는게 좋은 코드이다.
def get_max(left, right):
    max_val = left
    
    if max_val < right:
        max_val = right        

    return max_val

#두 개의 정수를 입력받아서 두 수 중에서 더 작은 수를 찾아서 리턴하는 함수 
def get_min(left, right):
    min_val = left
    
    if min_val > right:
        min_val = right        

    return min_val

#거듭제곱 구하여 해당하는 값을 반환하는 함수. 
def get_power(x, y):
    result = 1
    for i in range(y):
        result *= x
    return result
