'''

더블 루프를 이용하여 아래와 같이 출력하는 프로그램을 작성하시오.

출력 결과

    *
   ***
  *****
 *******
*********

{^[범위]} format()
중앙 정렬.


'''

# #더블 루프
# for y in range(5, 0, -1):
#     for x in range(10):
#         if (x >= y and x <= (10 - y)):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print("")

for y in range(1, 6):
    for x in range(5 - y):   
        print(" ", end="")
    for x in range(1, y * 2):     
        print("*", end="")
    print("")



# #format 사용.
# print("-" * 40)
# star = "*"
# space = " "

# for i in range(5):
#     move = 5 - i
#     print("{0}{1}".format(space * move , star * ((i * 2) + 1)))

print("-" * 40)
for i in range(1, 11, 2):
    print("{:^10}".format("*" * i))
   

'''

    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *

'''

print("-" * 40)
for y in range(1, 6):
    for x in range(5 - y):   
        print(" ", end="")
    for x in range(1, y * 2):     
        print("*", end="")
    print("")
for y in range(5):
    for x in range(y):   
        print(" ", end="")
    for x in range(10, (y * 2) + 1, -1):     
        print("*", end="")
    print("")