'''

사용자로부터 10진수를 입력받아서 2진수 문자열로 변환하여 반환하는 함수 dec_to_bin(num)를 작성하고 테스트

'''

def dec_to_bin(num):
    bin = ""
    while num != 0:
        value = num % 2
        if value == 0:
            bin = "0" + bin
        else:
            bin = "1" + bin
        num = num // 2
    return bin

#num = int(input("10진수를 입력하세요 :"))
#print(f"10진수 {num}의 2진수 변환 값은 {dec_to_bin(num)}입니다.")


print("=" * 40)
#파이썬에서 제공하는 진법 변환 함수들
print(bin(10)) #2진수로 변환하는 내장 함수.
print(oct(10)) #8진수로 변환하는 내장 함수.
print(hex(10)) #16진수로 변환하는 내장 함수.

print("=" * 40)
#2진수, 8진수, 16진수의 값을 10진수로 변환하는 방법
print(int("0b1010", 2))
print(int("0o12", 8))
print(int("0xa", 16))