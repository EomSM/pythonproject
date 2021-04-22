# 기본형 4자리
# 정수 실수
age = 100
weight = 99.9
sum = age + weight #더하기연산자
print(sum)
sum2= age + weight
print(sum2)

temp=input('현재 온도는>> ')
print(type(temp))
temp2=float(temp)
print(type(temp2))

if temp2>20:
    print("더워")
else:
    print("아직 괜찮아")

# 형변환(Casting)
# 문자로 바꾸는 거 Str
# 정수로 : int
# 실수로: float

# 문자
company = '메가'
print(company)# 프린트 후 엔터 적용됨
print('우리 회사는', company)

# 논리
food=True
food2=1#0

if food==food2:
    print('아침 먹어서 다해')
else:
    print('배고프겠다')