'''

변수의 두 개의 값을 서로 바꾸는 예제

'''

num1 = 100
#str1 = "100"
#float1 = 100.777

num2 = 200

#데이터 타입을 확인하는 함수. type()
#print(type(num1)) 
#print(type(str1))
#print(type(float1))

print("num1 : ", num1, "num2 : ", num2)

def exchange_number(left, right):
    temp_val=left
    left=right
    right=temp_val

    return (left, right)


num1, num2 = exchange_number(num1, num2)

print("num1 : ", num1, "num2 : ", num2)
