'''
문제9. 
문자열을 입력 받아, 해당 문자열을 문자 순서를 뒤집어서 반환하는 함수 reverse(s)을 작성하세요.
실행결과:

입력> Java Programming!
결과> !gnimmargorP avaJ
'''

def reverse(s):
    result = s[::-1]
    return result

while True:
    s = input("입력> ")

    if s.isdigit() is False:
        print("결과> ",reverse(s))
        break
    else:
        print('문자를 입력 하세요')
        continue

