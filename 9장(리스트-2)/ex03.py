'''

값으로 호출, 참조로 호출의 차이점

'''

def func(x : int) -> None:
    print(f"x = {x} address = {id(x)}")
    x += "하세요"
    print(f"x = {x} address = {id(x)}")

#y = 10 #정수형(변경 불가능한 객체)
y = "안녕" #문자형(변경 불가능한 객체)

print(f"y = {y} address = {id(y)}")
func(y) #함수 호출(값에 의한 호출)
print(f"y = {y} address = {id(y)}")

print("=" * 40)

def func_list(x : int) -> None:
    print(f"x = {x} address = {id(x)}")
    x.append("하세요") 
    print(f"x = {x} address = {id(x)}")

y = ["안녕"] #리스트형(변경 가능한 객체)

print(f"y = {y} address = {id(y)}")
func_list(y) #함수 호출(값에 의한 호출)
print(f"y = {y} address = {id(y)}")