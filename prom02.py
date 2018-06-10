while True:
    innum = input("수를 입력하세요 : ")
    if innum.isdigit():
        num = int(innum)
        if num == 0:
            break
        elif num % 2 == 0:
            print('짝수')
            print("Process finished with exit code 0 ")
        elif num % 2 == 1:
            print('홀수')
            print("Process finished with exit code 0 ")
    else:
        print('정수가 아닙니다')
        print("Process finished with exit code 0 ")
        continue
    