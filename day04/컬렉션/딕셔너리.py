me = {'이름':'hong', 'age':100, 'height':180.5}
you = {'이름':'kim', 'age':90, 'height':170.5}
#딕셔너리, {키:값, 키:값}
print(me['이름'])
print(me['age'])
me['age'] = 101
print(me)
print(you)

he = dict()
he['이름'] = 'song'
he['age']='200'
he['height']=130.4
he['weight']=100.5
print(he)
del he['height']
print(he)
he['키']=170.4
print(len(he))
print(he.keys())

for x in he:
    #print(x) #key만 출력
    print(me[x])

scores = {"철수": 90, "민수": 85, "영희": 80}

# keys
keys = scores.keys()
for k in keys:
    print(k)

# values
values = scores.values()
for v in values:
    print(v)