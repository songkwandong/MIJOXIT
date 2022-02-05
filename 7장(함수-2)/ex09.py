'''

매개변수는 함수의 선언부에 존재하며 함수가 호출될 때 비로소 메모리에 할당이 된다.
함수가 종료되면 매개변수도 소멸이 된다.

매개변수도 지역변수의 일종이다.

'''

def list_test(my_list:list) -> None:
    #매개변수로 넘어온 my_list에 새로운 리스트를 할당한다.
    print(f"함수 내부에서의 my_list 값 할당 전 주소값 : {id(my_list)}")
    #매개변수로 넘어온 메모리의 주소를 버리고 새롭게 할당한 리스트의 주소를 가지게 된다,
    my_list = [1, 2, 3, 4]
    print(f"함수 내부에서의 my_list 값 할당 후 주소값 : {id(my_list)}")
    print(f"함수 내부에서의 my_list : {my_list}")
    
    return

#my_list 타입은 list이므로 변경가능객체(immutable object)
my_list = [100, 200, 300, 400]
print(f"함수 호출전 my_list의 주소값 : {id(my_list)}")
list_test(my_list)
print(f"함수 호출후 my_list의 주소값 : {id(my_list)}")
print(f"함수 외부에서의 my_list : {my_list}")

