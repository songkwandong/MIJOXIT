'''

일회용 패스워드 생성기를 이용하여서 3개의 패스워드를 생성하여 출력하는 프로그램을 작성.
패스워드의 길이는 6개자리로 한정한다.

난수가 발생되는 범위값 지정을 아래와 같이 한다.
난수 발생 문자열 : "0123456789"

'''

from random import randint, randrange

random_range = "0123456789"
def rand_passwd_make_list(random_range):
    passwd_list = []
    for i in range(6):
        passwd_list.append(random_range[randint(0, 9)])
    
    passwd = "".join(passwd_list)
    return passwd
    
def rand_passwd_make_str(random_range):
    passwd = ""
    for i in range(6):
        passwd += random_range[randrange(len(random_range))]

    return passwd

print(f"랜덤 패스워드는 {rand_passwd_make_list(random_range)}입니다. ")
print(f"랜덤 패스워드는 {rand_passwd_make_str(random_range)}입니다. ")