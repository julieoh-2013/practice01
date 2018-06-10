import random

b = True

while b:
    rnum = random.randint(1,100)
    print("수를 결정하였습니다. 맞추어 보세요")
    print("1-100")
    print(rnum)
    c = True
    while c:
            num = (int)(input(">>"))
            if num == rnum:
                print("맞았습니다.")
                c=False
                break
            else:
                if num > rnum:
                    print("더 낮게")
                else:
                    print("더 높게")

    yn=input("다시 하시겠습니까(y/n)>>")
    if(yn=='y'):
        continue
    else:
        b=False
        break