food_list = ['맛나피자', '새로운피자', '대왕햄버거', '군대햄버거']
# print(food_list[-1])# 끝에서부터 가져오기
# #피자집 개수, 햄버거집 개수 프린트
# #1. 리스트에서 '피자' 항목 있는[포함하는] 요소 검색 > 개수 세서 count로.  > 출력
# #. 이 때에 변수형 문자열 그대로 '피자'~검색하면 검색값 0으로 나옴.  부분만 검색하는건데?
# # print(food_list[-4:-2])
# # last_food = food_list[-1]
# # print(last_food[:-3])
# print(food_list[2:])
# last_food=food_list[-1]
# print(last_food[2:])

pizza = 0
burger = 0

for i in range((len(food_list))):
    if len(food_list[2:]) == 2: #"피자"
        pizza = food_list.count('피자')
        pizza = pizza+1
    elif len(food_list[2:]) == 3: #"햄버거"
        burger = food_list.count('햄버거')
        burger = burger+1

print('피자가게개수: ', pizza)
print('버거가게개수: ', burger)
# # pizza = 0, hamburger=0
#pizza = food_list.count('피자')
