'''

피보나치 수열을 구하는 프로그램 만들기
피보나치 수열이란 앞의 2개의 수를 더해서 다음 수를 결정짓는 수열이다.

ex) 사용자로부터 13을 입력받고 난 뒤 피보나치 수열의 값 : 1 1 2 3 5 8

'''

n = int(input("값을 입력하세요:"))

n1 = 1
n2 = 1
n3 = 1

for i in range(1, n):

    if i < 3:
        n3 = 1
    else:
        n3 = n1 + n2
    n1 = n2
    n2 = n3

    if n3 == n:
        break
    print("{}".format(n3), end=" ")
    


        



    