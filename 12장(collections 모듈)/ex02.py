'''

deque와 list의 성능 테스트 비교.

'''

from collections import deque
import time

#저장 성능 측정
#append의 경우보다 insert가 훨씬 차이남..
deque_test = deque()
start = time.time() #시작 시간을 저장(second 단위)

for i in range(1000000):
    deque_test.append(i)

end = time.time()
print(f"deque append 시간: {end - start}초")

list_test = list()

start = time.time() 

for i in range(1000000):
    list_test.append(i)

end = time.time()
print(f"list append 시간: {end - start}초")

# 1억건 결과
# deque append 시간: 8.453715085983276초
# list append 시간: 9.526586532592773초

#추출 성능 측정
#pop의 경우보다 popleft vs pop(0)가 훨씬 차이남..
# print("=" * 40)
# start = time.time() #시작 시간을 저장(second 단위)

# for i in range(100000000):
#     deque_test.pop()

# end = time.time()
# print(f"deque pop 시간: {end - start}초")

# start = time.time() 
# for i in range(100000000):
#     list_test.pop()

# end = time.time()
# print(f"list pop 시간: {end - start}초")

# 1억건 결과 (?)
# deque pop 시간: 8.32776689529419초
# list pop 시간: 7.298295736312866초

print("=" * 40)
start = time.time() #시작 시간을 저장(second 단위)

for i in range(1000000):
    deque_test.popleft()

end = time.time()
print(f"deque popleft() 시간: {end - start}초")

start = time.time() 
for i in range(1000000):
    list_test.pop(0)

end = time.time()
print(f"list pop(0) 시간: {end - start}초")

# 백만건 결과
# deque popleft() 시간: 0.08252549171447754초
# 안나옴 ..

#결론은 list, deque를 성능 테스트시 데이터를 추가할 때
#deque가 훨씬 좋은 성능 발휘, 대용량일수록 더욱더 많은 차이가 발생.
#추출할 때는 역시 deque가 list보다 훨씬 빠른 성능을 보인다.
#데이터의 용량이 클수록 deque를 사용하는것이 더 좋다.
