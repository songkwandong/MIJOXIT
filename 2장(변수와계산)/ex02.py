'''

사용자로부터 참석하는 인원의 수를 받아 해당하는 인원의 수에 따라 
치킨은 인원당 1, 맥주는 인원당 2, 케잌은 인원당 4를 출력하는 
프로그램을 작성하시오

'''

#input() - 사용자한테 입력 받을 때 문자열 형태로 저장됨.
people_num = input("참석자 수를 입력하세요 : ")
print(type(people_num))

people_num = int(people_num)

chickens_num = people_num
beers_num = people_num * 2
cakes_num = people_num * 4

print("참석 인원수 :", people_num, "치킨 수: ", chickens_num, "맥주 수:", beers_num, "케잌 수:", cakes_num)
