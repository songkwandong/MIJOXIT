'''

중복(nested) if ~ else 구문
사용자로부터 ID를 입력받아서 등록되어진 아이디인지를 검사하는 프로그램을 작성하는데
등록된 아이디를 리스트 자료구조에 저장하도록 한다.
아이디가 등록되어 있다면 패스워드를 물어보는 프로그램을 작성

단 패스워드는 "1234"라고 가정하도록 한다.

'''

# id_list = ["kmn7789","kmn4456","gvc4456"]

# input_id = input("ID를 입력해주세요:")

# for i in range(0,len(id_list)):
#     if input_id == id_list[i]:
#         input_passwd = input("비밀번호를 입력해주세요.:")

# print("ID = {} Passwd = {} 입니다.".format(input_id, input_passwd))
        

id_list = ["kmn7789","kmn4456","gvc4456"]

input_id = input("ID를 입력해주세요:")

pw = "1234"
if input_id in id_list:
    input_passwd = input("비밀번호를 입력해주세요.:")
    if input_passwd == pw:
        print("{}님이 로그인하셨습니다.".format(input_id))
    else:
        print("Password Error!")
else:
    print("ID가 존재하지 않습니다.")