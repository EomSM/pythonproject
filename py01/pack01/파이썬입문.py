# -*- coding: utf-8 -*-
"""파이썬입문.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/EomSM/python_start/blob/main/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9E%85%EB%AC%B8.ipynb
"""

print('hello')

print('안녕하세요.', end=' ')
print('저는 홍길동입니다')

# 설명문, Ctrl+/ , comment, 주석.
# 입력:데이터를 파이썬 프로그램으로 가지고 옴.
# 처리: 적절한 처리
# 출력: 처리한 결과를 내보내는 것(모니터 화면 ; 파일로 저장 ; DB에 저장 ; 네트워크 전송 etc.)

name = input('이름을 입력하세요 >> ') # 간단한 처리(기호 사용) : 연산 = 연산자
#= : 대입연산자

print(name)

#소속나이이름
company = input('소속을 입력하세요 >> ' )
age = input('나이를 입력하세요 >> ')
name = input('이름을 입력하세요 >> ')
print(company, age, name)

location = '신촌'
number=2 #정수는 앞뒤 아무 기호 x
height=199.5 #실수도 앞뒤 기호 x
food_lunch=True #Py _를 붙이는 뱀표기법(sneak) ; 자바_소문자 T표시. foodLunch '낙타혹(camel)표기법' ; html & stql 두 개만 대소문자 구분x

age2=input('나이 입력>> ')
 #컴퓨터에서 입력한 데이터는 타입을 무조건 스트링으로 인식.
#Str->Int로 타입 변환 (casting 강제 캐스팅)
print('내년 나이', int(age2)+1)

number1=int(input('숫자1>> '))
number2=int(input('숫자2>> '))
print('더하기', number1+number2) #산술연산자
print('빼기', number1-number2)
print('곱하기', number1*number2)
print('나누기1', number1/number2) #%는 나머지 소수점만만
print('나누기2', number1//number2) #실수 부분 잘라내고 정수

me= '커피'
me2='우유'
print(me+me2)#결합연산자, 문자열로.
price=1000 #str으로 처리
print(me +'가격은 '+ str(price)+'원')

coffee_price=5000
coffee_person=5
sum=coffee_price * coffee_person #변수 var(저장공간, 저장공간이름=>변수명)

if sum>=20000:
 print("2천원을 할인해드립니다")
 print(sum-2000)
else:
 print("계산값을 다 지불")
 print(sum)

sum

principal = input("1년만기정기예금 얼마나 예치하시겠습니까?") 
#'20000'을 가져오는 명령어[input]필요
principal2 = int(principal)
print("원금이", principal2,"원이시군요")
interest = principal2*0.1
print("이자는", int(interest), "원입니다.")
sum=principal2+interest
print("원리합계는", int(sum), "원입니다.")

eng = int(input('영어점수'))
math = int(input('수학점수'))
korean = int(input('국어점수'))
print('세 과목의 합', eng+math+korean)
print('평균', int((eng+math+korean)/3))

time=int(input("지금은 몇시입니까?"))
if time<12:
  print("맛있게 드세요!")
else:
  print("점심후입니다")

id="root"
print (id=='root')
root=True
id2='root1'
print(id2=='root')

sticker_price=1000
sticker_amount=3
bookmark_price=2500
bookmark_amount=4
sum = sticker_price*sticker_amount+bookmark_price*bookmark_amount
print("정가", sum)
discount = sum*0.1
print("할인받은 금액", discount)
print("내가 낸 금액", int(sum-discount))

id = 'root'
id2 = input("id입력") 

if id == id2:
  print ("로그인")
else:
  print ("X로그인")

# CPU가 덜 바빠지게 하는 것: RAM에 한번 더 저장을 시켜서 그 값을 불러오는 게 더 좋음.
# RAM= 변수[기본데이터: string(문자열)/int(정수)/float(실수)/boolean(논리형)]; 변수명
# 연산자(기호 로 보이는 것) : CPU가 할 수 있는 간단한 처리  - 제어문, 대연, 부품
# 1 대입: =,할당연산자 | 2 결합 : + | 3 산술: +-*/ // % | 4 비교 == != > < >= <= [[비교의 결과가 True/False로 나옴 => Boolean 논리형 data]] | 5 논리 and or
# 제어문(순차문 입력-처리-출력, 조건문 if / if~else / if~ elif~else, 반복문 while, for)

