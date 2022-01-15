
print("숫자 게임 시작.")

guess_number = 62

#input = get user input
exact_num = input("1~100 사이의 숫자 추측 해보셈.")
print(exact_num)

#문자열로 넘어온 값을 int() 사용하여 숫자로 변경
guess = int(exact_num)

if guess == guess_number :
    print("Good~ b")
else :
    print("Fail~ --;")

print("--- The End ---")
