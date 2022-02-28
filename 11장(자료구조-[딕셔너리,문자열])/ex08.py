'''

문자열 안에 있는 문자의 개수, 숫자의 개수, 공백의 개수를 계산하는 프로그램을
작성.

문자열을 입력하시오.:A picture is worth a thousand words.
{'digits':0, 'spaces':6, 'alphas':29}

'''


def main():
    #string = input("문자열을 입력하시오.:")
    string ="A picture is worth a thousand words."
    result = check_word(string)
    print(result)

def check_word(string: str) -> dict:
    word_dict = dict()
    word_dict['digits']=0
    word_dict['spaces']=0
    word_dict['alphas']=0

    for i in range(len(string)):
        if string[i].isalpha():
            word_dict['alphas'] += 1
        elif string[i].isdigit():
            word_dict['digits'] += 1
        elif string[i].isspace():
            word_dict['spaces'] += 1
        else:
            print("무슨 문자죠?")

    return word_dict

if __name__ == "__main__":
    main()