'''
키보드에서 5개의 정수를 입력 받아 
리스트에 저장하고 평균을 구하는 프로그램을 작성하시오

실행결과 : 
> 1
> 2
> 3
> 4
> 5
평균: 3.0
'''
i=0
lst=[]
total=0
while(i<5):
    num = (int)(input(">"))
    lst.append(num)
    total += num
    i+=1

print("평균: {}".format(total/len(lst)) )


