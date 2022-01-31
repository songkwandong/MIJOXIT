'''

섭씨 온도를 화씨 온도로 변환하여 반환하는 함수 ftoc()를 작성하시오.

공식 : 화씨(F) = (9.0/5.0) * 섭씨(C) + 32

main 사용법.

'''

def ctof(c):
    return ((9.0/5.0) * c) + 32
def ftoc(f):
    return (5.0 * (f - 32))/9.0

def main():
    c = int(input("섭씨를 입력하세요:"))
    f = int(input("화씨를 입력하세요:"))
    print(f"섭씨={round(ftoc(f), 2)}, 화씨={ctof(c)}")

main()