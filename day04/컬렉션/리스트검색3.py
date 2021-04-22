#위 리스트에 들어간 값으로 사원정보를 각각 출력해보기.: 입력이 여러개, 목록일 때.
#1. 리스트에서 요소를 하나씩 꺼냄
#2. 꺼낸 요소 중 부서, 직급 추출
#3. 출력

member = ['a110', 'b230', 'c340']
#index를 쓸 경우 리스트의 개수를 찾아음: <- for문으로 반복할 range 정하기 위해
#각각의 항목으로 나오기. result 변수를 새로 만들어줘서 꺼내기?
#각 항목에서의 첫번째 chrt:부서 두번째:직급으로 가져옴
# 출력을 순서대로(a~, b~, c~)

#방법 1
for code in member:
    print(code)
    dep = code[0]
    deg = code[1]

    # print('1. dep: ----', dep)
    if dep == 'a':
        result = '기획부'
    elif dep == 'b':
        result = '개발부'
    elif dep == 'c':
        result = '인사부'
    else:
        print('\n해당 부서 존재하지 않음.')

    # print('2. deg: ---', deg)
    if deg == '1':
        result = result + " " + "사장"
    elif deg == '2':
        result = result + " " + "팀장"
    elif deg == '3':
        result = result + " " + "사원"
    else:
        print('\n해당 직급 없음.')  # for 문이나 While문으로도 처리 가능

    print('=========================')
    print('당신은 ', result)

# #방법2
for index in range((len(member))):
    print(member[index]) #code
    code=member[index]
    dep = code[0]
    deg = code[1]

    print('1. dep: ----', dep)
    if dep == 'a':
        result = '기획부'
    elif dep == 'b':
        result = '개발부'
    elif dep == 'c':
        result = '인사부'
    else:
        print('\n해당 부서 존재하지 않음.')

    print('2. deg: ---', deg)
    if deg == '1':
        result = result + " " + "사장"
    elif deg == '2':
        result = result + " " + "팀장"
    elif deg == '3':
        result = result + " " + "사원"
    else:
        print('\n해당 직급 없음.')  # for 문이나 While문으로도 처리 가능

    print('=========================')
    print('당신은 ', result)
