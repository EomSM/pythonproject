food_list = ['맛나피자', '새로운피자', '핫핫피자', '대왕햄버거', '군대햄버거', '리아햄버거']

#방법1
pizza = 0
ham = 0 # 얘네 안 넣어줘서 안됐네...?
for x in food_list:
    if '피자' in x:
        pizza= pizza+1
    elif '햄버거' in x:
        ham= ham+1
print('피자개수: ', pizza)
print('버거개수: ', ham)


#방법2
pizzza =0
burgger = 0

for i in food_list:
    food = i[2:]
    if food == '피자':
        result = pizzza
        pizzza = pizzza+1
    elif food == '햄버거':
        result = burgger
        burgger = burgger +1
print('피자가게개수: ', pizzza) # 값이 1 적게 나오는 신비
print('버거가게개수: ', burgger)


# # for x in food list
# #     print('피자' in x)
# #
# # print('-------')
# #
