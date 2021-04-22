#내가 좋아하는장소, 싫어하는 장소, 내가 가고 싶은 장소
place = {'좋아' : '대학로', '싫어':'강남', '가고파':'집'}
print(place['좋아'])
place['가고파'] = '신촌'
print(place)
print(place.keys())
for x in place:
    print(x)

#사전만들기
word = dict()
word['사랑']='love'
word['우정']='friendship'
word['질투']='envy'
word['이별']='farewell'
word['꽃']='flower'
print(word)
print(word['꽃'])
print(word['우정'])

#전체학기 성적(1:100 2 :50 3: 88 4 :99)
#2학기는?
#전체 중 85 넘는 학기 출력
score= {'1학기':100, '2학기':50, '3학기':88, '4학기':99}
print(score['2학기'])
values= score.values()
for value in values:
    if value > 85:
        print(value, end=" ")

for y in score:
    if int(score[y])>85:
        print('85점이 넘는 학기는', y, score[y], end=" ")
        print(y, score[y])
    else:
        pass

keys=score.keys()
for x in keys:
    if score[x] > 85:
        print(x, end=" ")