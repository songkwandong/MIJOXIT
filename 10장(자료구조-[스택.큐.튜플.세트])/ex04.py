'''

함수를 만들어서 Queue 실습하기


'''

#큐에 저장하는 함수
def offer(data: list, n: int): # data는 저장할 장소(list), n 은 저장할 값
    data.append(n)

#큐에서 삭제하는 함수
def poll(data: list):
    if len(data) > 0:
        return data.pop(0)
    return False

def offer_insert(data: list):
    for i in range(1, 5):
            offer(queue, i)
            print(f"현재 큐의 상태: {queue}" )
    
def poll_delete(data : list):
    for i in range(1, 5):
            poll(queue)
            print(f"현재 큐의 상태: {queue}" )

if __name__ =="__main__":
    queue = []
    offer_insert(queue)        
    print("=" * 40)
    poll_delete(queue)        
    