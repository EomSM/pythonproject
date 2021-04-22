#import bs4
from bs4 import BeautifulSoup
from urllib import request #인터넷 접속

con = request.urlopen('https://finance.naver.com/item/main.nhn?code=005930')#연결부품획득 : 변수에 넣어줘야
# print('1. 연결 성공', con)
name='삼성전자' # txt 파일로 저장하자
#삼성전자 주가를 가져오는 것. 향후 같은 ui에서 다른 코드 가져올 것: for문 사용


doc= BeautifulSoup(con, 'html.parser') #받은 것을 html문서로 분석해라
#print('2. 받은 것 프린트 >> ', doc)
#doc 안에는 네이버.컴의 첫페이지인 index.html의 소스가 통째로 들어감.

span_code=doc.select('span.code')#이 속에서 a.nav를 추출. 검색의 결과는 리스트!
print(span_code) #a.는 부가적 데이터 : 메타데이타 metadata(옷 - 태그, 이 페이지 - a 태그)
# print('code의 개수 ',len(span_code))
code=span_code[0].text
print('코드: ',code)

# div_today= doc.select('div.today') #검색의 결과 리스트임
# #print(len(div_today))
# today1=div_today[0].select('span.blind') #검색의 결과는 리스트임 #오타 좀 안 났으면 좋겠다
# print(today1[0].text)

span_blind=doc.select('span.blind')
print(len(span_blind))
# print(span_blind[0])
# print(span_blind[1])
# print(span_blind[2])

for index in range(len(span_blind)):
    print(index, ':', span_blind[index].text)

#  / 고가/ 시가/ 저가
# yes, high, low, start 변수로 넣어주기
yes = span_blind[15].text
print('전일: ', yes)
high = span_blind[16].text
print('고가: ', high)
start=span_blind[19].text
print('시가: ', start)
low=span_blind[20].text
print('저가: ', low)

# all=doc.select('div.today span.blind') #div 밑 어딘가에 있을 span.blind를 이중일 때 한 번에 검색하는 방법. doc() 하고 안에 '_ 스페이스 ㅡ'
# # #변수가 아니라 태그값이라 _가 아닌 . 이런 거 확인!
# print(len(all))
# print(all[0].text)
# # 중간중간 확인, 찍어보기.

#파일을 쓰기 위한 저장. 파일이 저장되고 덮어씀
file = open(name+'.txt', 'w')
file.write(code + '\n')
file.write(yes + '\n')
file.write(high + '\n')
file.write(start + '\n')
file.write(low + '\n')
file.close()
