hobby = [] #hobby 리스트. 현재 데이터 x
hobby.append('코딩') #'코딩'이라는 데이터 추가.
print('개수>', len(hobby)) #현재 리스트의 개수 출력 > 1
hobby.append('등산') #'등산' 데이터 추가
print('개수>', len(hobby)) #현재 개수 =2개.

for _ in range(3): #변수를 지정 x,  범위를 3번까지 for문을 반복하여 수행, '새로운 취미'를 추가하도록.
    data = input('당신의 새로운 취미는 >> ') #입력값을 data에 넣겠다.
    hobby.append(data) #data를 hobby에 추가하겠다.

print('개수', len(hobby)) #개수 출력
print() #for문 마감

for x in (hobby):#for-each #x 변수를 hobby리스트에서
    print(x) #x변수를 출력
