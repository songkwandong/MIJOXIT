'''

기본적인 파일 입출력 실습

'''

data = []
fp = open("C:\\Users\\gvc44\\Desktop\\coding\\MIJOXIT\\test.txt", mode="r", encoding="UTF-8") 

#print(type(fp))
#print(fp)

#readlines() 메서드는 파일의 저장된 내용을 한번에 다 읽는다.

for line in fp.readlines():
    #strip() 메서드는 원래 문자열의 양쪽 공백을 제거하는 역할을 하지만,
    #파일을 읽어들일때는 엔터키 제거를 해준다.
    data.append(line.strip())

print("파일에서 읽은 내용입니다.")
print(data)

#프로그램에서 리소스를 다 사용했으면 반드시 close()메서드를 호출하도록 한다.
fp.close()

#파일에 내용쓰는 방법
#파일의 모드가 w인 경우는 기존파일의 내용을 덮어써버린다.
fp = open("C:\\Users\\gvc44\\Desktop\\coding\\MIJOXIT\\test.txt", mode="w", encoding="UTF-8") 
fp.write("우리는 파이썬을 공부합니다.")
fp.write("\n저희도 파이썬을 공부합니다.")
print("쓰기 완료")

fp.close()

#기존 파일의 내용에 추가를 해준다.
fp = open("C:\\Users\\gvc44\\Desktop\\coding\\MIJOXIT\\test.txt", mode="a", encoding="UTF-8") 
fp.write("\n 11. 우리는 파이썬을 공부합니다.")
fp.write("\n 22. 저희도 파이썬을 공부합니다.")
print("추가 완료")

fp.close()

#csv 파일 읽는 방법
import csv
fp = open("C:\\Users\\gvc44\\Desktop\\coding\\MIJOXIT\\sample.csv", mode="r") 
reader = csv.reader(fp)

for txt in reader:
    print(txt)
fp.close()
