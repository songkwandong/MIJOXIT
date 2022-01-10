'''

if문만 사용시에는 flag 확인 용도로 사용.
몇 십개의 if문이 존재하더라도 CPU는 모든 if문을 참조한다.
그러므로, 다량의 if문은 app 프로그램의 성능을 다운.

'''

score = 80

# if score >= 90:
#     print("점수가 90점 이상입니다. 학점은 A입니다.")    
# if score >= 80:
#     print("점수가 80점 이상입니다. 학점은 B입니다.")
# if score >= 70:
#     print("점수가 70점 이상입니다. 학점은 C입니다.")
# if score >= 60:
#     print("점수가 60점 이상입니다. 학점은 D입니다.")

if score >= 90:
    print("점수가 90점 이상입니다. 학점은 A입니다.")    
elif score >= 80:
    print("점수가 80점 이상입니다. 학점은 B입니다.")
elif score >= 70:
    print("점수가 70점 이상입니다. 학점은 C입니다.")
elif score >= 60:
    print("점수가 60점 이상입니다. 학점은 D입니다.")
else :
    print("점수가 60점 미만입니다. 학점은 F입니다.")
    