'''
키보드에서 정수로 된 돈의 액수를 입력 받아 
오만 원권, 
만원 권, 
오천 원권, 
천원 권, 
500원짜리 동전, 
100원짜리 동전, 
50원짜리 동전, 
10원짜리 동전, 
1원짜리 동전 
각 몇 개로 변환 되는지 작성하시오.

출력 결과 : 

금액: 67879

50000원 : 1개
10000원 : 1개
5000원: 1개
1000원: 2개
500원: 1개
100원: 3개
50원:1개
10원:2개
5원:1개
1원:4개

'''
money = int(input("금액: "))
print(money)
balence =0
cnt =0
change={}

l = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 1]

for  num in l:
    if  money >= num:
        n = money // num
        change[num]=n
        money = money - (n*num)
        print(money)
    
for k, v in change.items():       
    print("{}원 : {}개".format(k,v))