'''

정수를 입력받아서 시, 분, 초로 변경하는 프로그램
input ex) 3671

'''

time = int(input("정수를 입력하세요 :"))

second = time % 60
minute = (time // 60) % 60
hour = (time // 60) // 60 

print("시 : {},  분: {},  초: {}".format(hour, minute, second))