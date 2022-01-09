'''

문자열에 대한 실습
큰따옴표 (double quotation)로 묶으면 문자열이 됨
작은따옴표 (single quotation)로 묶어도 문자열이 됨

웬만하면 큰따옴표로 사용하자!

섞어서 사용하면 EOL(End Of Line) 에러가 난다.

\ = escape 문자. 뒤에오는 문자를 문자 자체로 변경한다.
\n = 개행
\t = tab
r"" = 문자열안의 이스케이프 문자들의 기능을 제거, 문자 자체로 사용.

문자열의 길이(한글, 영어 상관 x)를 알고자 한다면 len() 함수 이용

'''

# welcome = "Happy 유희열 2021"
# print(welcome)

# welcome = 'Happy 유희열 2021'
# print(welcome)

message = "은혁이가 \"안녕하세요\"라고 인사했습니다."
print(message)

message = "은혁이가 '안녕하세요'라고 인사했습니다."
print(message)

message = '은혁이가 "안녕하세요"라고 인사했습니다.'
print(message)

message = 'doesn\'t'
print(message)

message = "\"yes,\" I can Do It!"
print(message)

message = "First\nSecond\nThird"
print(message)

message = "c:\\temp\\name"
print(message)

message = r"c:\temp\name"
print(message)

message = "World"
print("문자열의 길이 :{}".format(len(message)))

message = "한글"
print("문자열의 길이 :{}".format(len(message)))
