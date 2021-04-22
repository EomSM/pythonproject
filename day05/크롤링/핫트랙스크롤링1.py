#import bs4
from bs4 import BeautifulSoup
from urllib import request #인터넷 접속

name_list = ['크라잉넛', '한영애', 'U2']
code_list = ['8809064223279', '8809064223415', '0602507316822']
for index in range(len(code_list)) :
    con = request.urlopen('http://www.hottracks.co.kr/ht/record/detail/'+code_list[index])#연결부품획득 : 변수에 넣어줘야

    doc= BeautifulSoup(con, 'html.parser')

    artist = doc.select('div h2.tit')
    # print(artist)
    ori_price=doc.select('span.ori_price')
    # print(ori_price)
    price=doc.select('div.price strong')
    # print(price)
    point=doc.select('span.w100')
    # print(point)


    artist = artist[0].text
    ori_price = ori_price[0].text
    price = price[0].text
    point = point[0].text

    art2 = artist.strip().split(sep='-')
    art3 = art2[0]
    title = art2[1].strip()

    print('가수: ', art3)
    print('제목: ', title)
    print('원가: ', ori_price)
    print('가격: ', price)
    print('적립포인트: ', point)

    file = open(name_list[index] + '.txt', 'w')
    file.write(name_list[index] + '\n')
    file.write(art3 + '\n')
    file.write(title + '\n')
    file.write(ori_price + '\n')
    file.write(price + '\n')
    file.write(point + '\n')

    file.close()

    print(name_list[index])
    print('-----')
    print()