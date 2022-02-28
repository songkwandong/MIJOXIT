'''

CSV 파일은 split() 메소드로 이용하여 파싱될 수 있다.
CSV 파일을 읽는 프로그램을 작성.
CSV(comma-separated values) , 로 분리해야한다.

'''

def main():
    f_name = open(file = "C:\\Users\\gvc44\\Desktop\\coding\\MIJOXIT\\sample.csv" \
            ,mode="r"
    )
    # read() : 파일을 처음부터 끝까지 읽을 때 사용.
    # readline() : 파일의 내용을 한 줄 씩 읽어들일때 사용.
    # readlines() : 파일을 읽으면 한 줄,한 줄이 각각 리스트의 원소로 들어감.

    for line in f_name.readlines():
        #공백 문자 제거.
        line = line.strip()
        print(line)
        print(type(line))

        #한 라인을 단어로 분리.
        words = line.split(",")
        for word in words:
            print(f"  {word}")
    f_name.close()


if __name__ == "__main__":
    main()