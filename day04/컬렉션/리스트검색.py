my_life = '나는 열심히 살자가 인생의 목표예요.!'

print(my_life[0])#인덱싱:0번 글자 1개 추출
print(my_life[0:4])#범위로 슬라이싱 0~4까지 글자 추출
#Str을 특정 기호(공백)으로 나누어 놓을 수 있음 str 5개 단어로 분리. Str 다섯개의 리스트로.
my_life_list = my_life.split(sep=' ')#Str 리스트. sep 구분자, space로. 앞의 것을. ()의 기준으로, 나누어라.
#['나는', '열심히', ...] <- 이 결과를 변수로 만들어서 메모리에 저장해주어야.
print(my_life_list[0])
print(my_life_list[1])

#.주민번호
social_no = '920101-1037515'
#이런 번호는 int로 해서 자리수 갖고 계산하는 게 아니라 Str으로 잡는다는 거
year = social_no[0:2]
#92라는 숫자로 나이를 추출하고 싶음 : 1. str('92')->int 캐스팅
year2 = int(year)
#2. 나이계산 : 1900을 더해주기
age = 2021 - (1900+year2)
print('당신의 나이는', age, '세')

gender = social_no[7] #'1'을 추출
#gender2 = int(gender) <# #숫자로 바꾸는 과정이 꼭 필요할까? 꼭 1이 아니여도 표시는 되는 숫자. 문자 한 글자. 그래서 '1'처럼 감싸주기.
if gender == '1' or gender == '3': #논리연산자
    print("남성")
elif gender == '2' or gender == '4': #입력에 의한 것이라면, 잘못치는 경우 발생. 그걸 감안해서 하는 게
    print("여성")
else:
    print("잘못된 입력값")

