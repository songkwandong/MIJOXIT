'''

텍스트 파일을 읽어서 단어를 얼마나 다양하게 사용하여 문서를 작성하였는지를
계산하는 프로그램 작성

입력 파일 이름: words.txt
사용된 단어의 개수 : 18



'''


def processing(word):
    out_str =""
    for i in word:
        if i.isalpha():
            out_str += i
    return out_str.lower()


file_name = "words.txt"
fp = open(f"C:\\Users\\gvc44\\Desktop\\coding\\MIJOXIT\\10장(자료구조-스택.큐.튜플.세트))\\{file_name}", mode="r", encoding="UTF-8") 
data = set()

for line in fp.readlines():
    #line_string = line.strip()
    #print(line)
    for i in line.split():
        data.add(processing(i))
    
print(f"입력 파일 이름: {file_name}")
print(f"사용된 단어의 개수: {len(data)}")
print(data)
fp.close()