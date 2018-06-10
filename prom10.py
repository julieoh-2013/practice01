'''
주어진 if 문을 dict를 사용해서 수정하세요.
'''

dic = {'오뎅':300,  '순대':400, '만두':500}

menu = input('메뉴: ')


if menu in dic.keys():
    print('가격: {0}'.format(dic[menu]))
else:
    print('메뉴명을 확인해주세요.')


