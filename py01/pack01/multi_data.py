food= ['아이스크림','아이스아메리카노','생수'] # food라는 이름의 리스트를 생성. 3개의 항목을 넣음.

# index 목차 로 각각의 위치 확인 가능.
print(food[0]) #리스트에서 1번째 항목을 출력
print(food[1]) #리스트에서 2번째 항목을 출력
print(food[2]) #리스트에서 3번째 항목을 출력
for i in range(0,3): #리스트의 범위 0, 부터 3 미만, 0,1,2 = 3개까지의 범위에서. ":"는 for문을 시직하겠다는 표기.
    print(food[i], end=' ') #food 리스트를 출력, #end 처리로 기본 출력값인 엔터를 띄어쓰기로 변경
print()# 7번째줄 for문을 종료

for x in food: #for-each # Food 리스트에서 x 변수를 설정
    print(x, end=' ') #x 변수 출력
print()
print('목록의 개수는 ', len(food),'개임.') #len 함수로 food 리스트의 개수 출력.


# Quiz_ 오늘 끝나고 할 일 5가지 목록으로. 2가지 방식으로 프린트
to_do=['저녁', '설거지', '빨래','스트레칭', '취침'] #to_do 리스트를 다음과 같이 작성.

for i in range(0,5): #0부터 시작하는데, 0,1,2,3,4 <- 5개. i를 0부터 5미만의 범위에서 for문을 시작.
    print(i, to_do[i],  end=' ') #to_do 리스트를 출력, 기본 출력값인 엔터를 띄어쓰기로 변경
print()
for x in to_do: #for-each, #to-do리스트 에 있는 데이터를 for문ㅇ느로.
    print(x, end=' ') # to_do 리스트 출력.
print()
print('목록의 개수는 ', len(to_do),'개임.') #목록 개수를 len으로 출력.
print()

for i in range(0,len(to_do)):
    print(i, to_do[i], end=' ')
