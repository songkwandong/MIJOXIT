'''


'''

#모듈을 활용하는 첫 번째 방법
import fibo


#모듈을 활용하는 두 번째 방법
#from fibo import fibo, sum
# from fibo import *

# fibo(100)
# print("")
# print("=" * 40)
# print(sum(10))

#위 두개의 차이점은 import를 사용하면 파일명.함수명()으로 호출되므로
#사용한 함수의 출처를 알 수가 있다.
#from fibo import *를 사용하면 파일명이 필요가 없다. 함수명으로 바로 호출이 가능하다.

#__name__은 내장 전역변수로 인터프리터가 만들어 놓은 것이다.
#print(fibo.__name__)

#실행파일에서는 __name__이라는 내장 전역변수는 __main__이라는 값을 지니게 된다.
#print(__name__)

def main():
    #fibo.py 모듈의 fibo()를 사용하겠다
    fibo.fibo(100)
    print("")
    print("=" * 40)
    #fibo.py 모듈의 sum()를 사용하겠다
    print(fibo.sum(5))

if __name__ == "__main__": #프로그램의 시작점이 되는 형태.
    main()
