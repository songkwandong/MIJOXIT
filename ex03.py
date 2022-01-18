'''

1부터 사용자가 입력한 수 num까지 더해서 합계를 구하는 프로그램을 for문을 이용해서 작성하시오.
+= 복합대입 연산자(값을 누적하거나 차감할 때 사용하는 연산자.)
'''

input_num = int(input("숫자를 입력해주세요."))

sum = 0

for i in range(1,(input_num + 1)):
    sum += i

print("1부터 입력한 {}까지의 합계는 {}입니다.".format(input_num,sum)) 