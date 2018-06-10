while True:
    innum = input("수를 입력하세요")
    num =0
    if innum.isdigit():
        num = int(innum)
        if num == 0:
            break
        elif num % 3 == 0:
            print('3의 배수입니다 ')
            print("Process finished with exit code 0")
        else:
            print('3의 배수가 아닙니다.')
            print("Process finished with exit code 0 ")
    else:
        print('정수가 아닙니다')
        print("Process finished with exit code 0 ")
        continue

