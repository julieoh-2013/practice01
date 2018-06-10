'''
반복문을 이용하여 369게임에서 박수를 쳐야 하는 경우의 수를 순서대로 화면에
출력해보세요. 1부터 99까지만 실행하세요.
'''

i =0
l=[3,6,9]
for i in range(1,100):
    if i<10:
        if i % 3 ==0:
            print(i,"짝")
    else:
        b1= i//10 in l
        b2= i%10 in l

        if b1 & b2 :
            print(i, "짝짝")
        elif b1 | b2:
            print(i, "짝")
        else:
            print(i)