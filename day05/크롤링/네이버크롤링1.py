#import bs4
from bs4 import BeautifulSoup
from urllib import request #인터넷 접속

con = request.urlopen('http://www.naver.com')#연결부품획득 : 변수에 넣어줘야
print('1. 연결 성공', con)
doc= BeautifulSoup(con, 'html.parser') #받은 것을 html문서로 분석해라
#print('2. 받은 것 프린트 >> ', doc)
#doc 안에는 네이버.컴의 첫페이지인 index.html의 소스가 통째로 들어감.

a_nav=doc.select('a.nav')#이 속에서 a.nav를 추출. 검색의 결과는 리스트!
print(a_nav) #a.는 부가적 데이터 : 메타데이타 metadata(옷 - 태그, 이 페이지 - a 태그)
print(len(a_nav))
print(a_nav[0])
print(a_nav[0].text) #a 태그 빼고 텍스트만 추출
print(a_nav[7].text)
print(a_nav[8].text)
print(a_nav[9].text)