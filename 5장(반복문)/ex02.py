'''

range() 함수 실습하기


1. range(x) 매개변수 1개짜리 함수를 이용.
2. range(start, stop) 매개변수 2개짜리 함수를 이용
3. range(start, stop, step) 매개변수 3개짜리 함수를 이용
누적을 하는데 stop값은 포함되지 않는다. 누적을 시킬 때 step 만큼 건너띄어 리스트를 생성한다.

문자열 실습
문자열도 시퀀스 대상에 포함된다. 하여 for문을 통해 문자를 추출하여 출력할 수가 있다.

'''

sum = 0

for i in range(10):
    sum = sum + i
print("1. 0~9 까지의 누계합 :{}".format(sum))
print("=" * 50)

sum = 0

for i in range(0,10):
    sum = sum + i
print("2. 0~9 까지의 누계합 :{}".format(sum))
print("=" * 50)

sum = 0

for i in range(0,10,2):
    sum = sum + i
print("3. 0~9 까지의 짝수 누계합 :{}".format(sum))
print("=" * 50)

s = "Song Kwan Dong"

print("=" * 50)
for i in s:
    print(i, end=" ")



