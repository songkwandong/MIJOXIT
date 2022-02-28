'''

str 클래스의 메서드 실습

split() : 문자열에서 단어(토큰)을 분리하고자 할 때 사용한느 메서드
인자값으로 구분자(seperator)를 주게 되면 주어진 구분자로 문자열을 분리한다.
기본 인자값 공백이다.

'''
#정규표현식을 사용하기 위해서 regex 모듈 사용
import regex 


string = "안녕 john 난 지금 학교 가고 있어"
li1 = string.split() #공백으로 분리.
print(type(li1))
print(li1)

string = "안녕,john,난,지금,학교,가고,있어"
li2 = string.split(",") #콤마로 분리.
print(type(li2))
print(li2)

#split()은 하나의 구분자만 사용가능.
string = "안녕/john,난,지금|학교,가고,있어"
li3 = regex.split("[/,|&]", string) #정규 표현식으로 분리
print(type(li3))
print(li3)

#문자열을 검사
string = "abcd1"
print(string.isalpha()) # 문자열이 영문자인지 확인하는 코드

string="12345"
print(string.isdigit()) # 문자열이 10진수인지 확인하는 코드
print(string.isdecimal()) # 문자열이 10진수인지 확인하는 코드

print("=" * 40)
string="abcd12345"
print(string.isalnum()) # 문자열이 영문자, 숫자인지 동시에 확인하는 코드.

print("=" * 40)
string="1/2"
print(string.isnumeric()) # numeric 굉장히 넓은 의미인데, 숫자값 표현 문자열을 인정해준다. 
#str 클래스에서 음수, 실수 판별하는 메서드는 없다.

print("=" * 40)
string=" "
print(string.isspace()) #공백인지 확인하는 것

#부분 문자열 검색 실습 
#endswith(문자열) 메소드는 인자값 문자열로 끝이 나면 True 리턴한다.
print("=" * 40)
#string = input("파이썬 소스를 입력해주세요 :")
if string.endswith(".py"):
    print("올바른 파일이름입니다.")
else:
    print("틀린 파일 이름입니다.")

print("=" * 40)
string = "2021-03-04.txt"
#startswith(문자열) 메소드는 인자값 문자열로 시작하면 True 리턴한다.
if string.startswith("2021"):
    print("2021년 파일입니다.")
else:
    print("2021년 파일이 아닙니다.")


print("=" * 40)
#string = input("영어 단어를 입력하세요 : ")
print(string.upper()) #대문자로 변경
print(string.lower()) #소문자로 변경
print(string.capitalize()) #앞 한글자만 대문자로 변경
print(string.title()) #앞 한글자만 대문자로 변경

print("=" * 40)
#format() 포맷{}을 만들어놓고 문자열을 생성하는데 사용.
string = "{}b{}"
print(string.format("a","c"))

print("=" * 40)
#join()는 리스트 같은 반복(iterable) 인자를 전달받아서 문자열로 연결하는데 사용
string=["a", "b", "c"]
print("!".join(string))

print("=" * 40)
#partition() 전달받은 인자값으로 문자열을 나눈다. 리턴타입은 튜플이다.
string = "kmn7789@gmail.com"
print(string.partition("@")) 

print("=" * 40)
#count()는 인자값으로 들어오는 값을 문자열에서 몇개 있는지 카운팅을 해준다.
#찾는 인자값이 없다면 0을 리턴.
string = "aaaabbbcc"
print(string.count("a"))
print(string.count("z"))

print("=" * 40)
#find() 메서드는 특정 첫 단어를 찾아서 인덱스를 리턴하고 없다면 -1를 리턴한다.
#index() 차이점은 특정단어를 찾으면 인덱스를 리턴, 없다면 에러를 발생.
string = "apple"
print(string.find("z"))
#print(string.index("z"))

print("=" * 40)
#문자열에서 공백을 제거하는 방법
#strip() : 양쪽 공백 제거, 탭 문자, 줄바꿈(enter)도 제거
#lstrip() : 왼쪽 공백만 제거, 탭 문자도 포함
#rstrip() : 오른쪽 공백만 제거 탭 문자도 포함
#단 메서드로 문자열 중간에 존재하는 공백은 제거할 방법이 없다.(함수를 만들어 사용)

string = "          aaa          ccccccccc bbbb ddd \tee      "
print(string)
print(string.strip())
print(string.lstrip())
print(string.rstrip())




























