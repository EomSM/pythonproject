# 순차문의 구조로 가져오면 좋다. 입력 - 처리 - 출력
#파이썬에서는 들여쓰기(indent, tab키 <> Shft+tab)로 포함관계를 나타낸다.
while True: #무한반복
    code = input('본인의 사원번호 입력하세요. 종료 : x를 넣으세요 ') #입력
    if code == 'x':
        print('시스템 종료')
        break #현재 반복문을 끝내라

    #a110 : a 부서 1 직급 10 고유번호
    #부서 a기획 b개발 c인사
    #직급 1사장 2팀장 3사원

    #a110, b230, c340 를 판별
    #처리
    # 1. 입력 데이터중 부서, 직급 추출
    # 2. 부서 값에 따라 부서 판별x
    # 3. 직급 값에 따라 직급 판별

    #실제로는 글로 스크립트 - 변수명, 파일명, 순서도 등을 다 정하는 설계 - 한 후에야 코딩을 실제로 함. 내가 지금 처리를 어떻게 해야 할 지 모르겠으면 일단 스크립트를 써라.

    dep = code[0] #부서 #split로 하면 리스트로 메모리를 잡히는거라 단어 단위로 할 때에 필요. 이번에는 한글자.
    deg = code[1] #직급
    result= '' # 찍어줄 스트링을 모아줄 변수. 최종적으로 프린트는 한번만 하기 위해.

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
    elif deg =='3':
        result = result + " " + "사원"
    else:
        print('\n해당 직급 없음.')     #for 문이나 While문으로도 처리 가능

    print('=========================')
    print('당신은 ', result)