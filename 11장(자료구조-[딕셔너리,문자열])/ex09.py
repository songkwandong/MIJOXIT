'''

머리글자어(acronym)은 NATO처럼
각단어의 첫글자를 모아서 만든 문자열이다.
사용자로부터 문장을 입력하면 해당되는 머리글자어를 출력하는 프로그램을 만들어보자

문자열을 입력하시오.

'''

def main():
    string = "North Atlantic Treaty Organization"
    #string = input("문자열을 입력하시오.")
    result = ""
    result = make_acronym(string)
    print(result)

def make_acronym(string:str) -> str:
    string_li = string.upper().split()
    
    acronym = ""
    for word in string_li:
        acronym += word[0]
    return acronym

if __name__ == "__main__":
    main()
