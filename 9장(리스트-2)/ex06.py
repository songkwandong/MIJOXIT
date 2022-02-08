'''

연락처 관리 프로그램 만들기

친구 추가시 연락처도 함께 추가하는 프로그램으로 업데이트 해보기.

'''

PRINT_FRIEND_LIST_ORDER_NUM = 1
ADD_FRIEND_LIST_ORDER_NUM = 2
DEL_FRIEND_LIST_ORDER_NUM = 3
CHANGE_FRIEND_LIST_ORDER_NUM = 4
QUIT_ORDER_NUM = 9


def print_order() -> None :
    print ("-" * 20)
    print ("1. 친구 리스트 출력")
    print ("2. 친구 추가")
    print ("3. 친구 삭제")
    print ("4. 이름 변경")
    print ("9. 종료")

def main():
    friends_list = []

    for i in range(0, 100): 
        print_order()
        order_num = int(input("메뉴를 선택하세요. :"))
        
        if order_num == PRINT_FRIEND_LIST_ORDER_NUM:
            print("친구 리스트는 다음과 같습니다.")
            print(friends_list)
        elif order_num == ADD_FRIEND_LIST_ORDER_NUM:
            friend_info_list = []
            
            friend_name = input("이름을 입력하세요. :")
            friend_phone_number = input("핸드폰 번호를 입력하세요. :")
            
            friend_info_list.append(friend_name)
            friend_info_list.append(friend_phone_number)
            
            friends_list.append(friend_info_list)

        elif order_num == DEL_FRIEND_LIST_ORDER_NUM:
            friend_name = input("삭제할 이름을 입력하세요. :")
            for i in range(len(friends_list)):
                if friend_name in friends_list[i]:
                    del friends_list[i]
                    break
                else:
                    print("삭제할 친구가 없습니다.")
        elif order_num == CHANGE_FRIEND_LIST_ORDER_NUM:
            old_friend_name = input("변경하고 싶은 이름을 입력하세요. :")
            new_friend_name = input("변경할 이름을 입력하세요. :")
            for i in range(len(friends_list)):
                if old_friend_name in friends_list[i]:
                    friends_list[i][0] = new_friend_name
                else:
                    print("변경할 친구가 없습니다.")
        elif order_num == QUIT_ORDER_NUM:
            print("프로그램을 종료합니다.")
            break
        else:
            print("다시 입력해주세요.")
        
if __name__ == "__main__":
    main()



