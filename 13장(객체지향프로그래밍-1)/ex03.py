from Person import *


if __name__ == "__main__":
    #기본 생성자 호출
    #기본 생성자는 호출되면 무조건 똑같은 초기값을 지니고 메모리에 생성
    #그리고 그 값을 변경하려면 직접 setter()나 인스턴스명.필드 = 값 을 대입을 하여
    #변경하여야하는 단점이 존재한다.
    
    person1 = Person()
    person1.__str__()

    print("=" * 40)
    person2 = Person()
    person2.__str__()

    print("=" * 40)
    print(f"person1.__name : {person1.get_name()}")
    person1.set_name("김길동")
    person1.age = 50
    print(f"person1.__name : {person1.get_name()}")
    print(f"person1.address : {person1.get_address()}")
    print(f"person1.age : {person1.get_age()}")
    #age는 __ 붙지않아서 public이므로 외부에서 접근, 변경이 가능하다.
    print(f"person1.age : {person1.age}")

    #같은 필드의 값을 가지고 있지만 서로 다른 인스턴스이다.
    # print(f"person1의 주소 : {id(person1)}")
    # print(f"person2의 주소 : {id(person2)}")

