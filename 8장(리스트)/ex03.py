'''

리스트는 다양한 데이터를 저장할 수 있다고 배웠다.
하지만 현업에서는 같은 종류(모델)의 같은 타입의 데이터를 저장하면서 사용한다.

리스트는 문자열도 저장할 수가 있다. 강아지를 많이 키우는 사람이 있다고 가정.
사용자로부터 강아지들의 이름을 저장하였다가 출력하는 프로그램

조건: 무한루프를 돌면서 엔터키가 입력이 되면 무한루프를 탈출한다.

'''

def input_puppy_names() -> list:
    puppy_name_list = []
    flag = True

    while flag:
        puppy_name = input("강아지의 이름을 입력하시오(종료시에는 엔터키):")
        if puppy_name == "":
            flag = False
            continue
        else:
            puppy_name_list.append(puppy_name)
    return puppy_name_list

def print_puppy_name_list(puppy_name_list : list) -> None:
    print(f"강아지들의 이름은 {puppy_name_list} 입니다.")
    return

def main():
    puppy_name_list = input_puppy_names()
    print_puppy_name_list(puppy_name_list)
    
if __name__ == "__main__":
    main()
