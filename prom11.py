'''
함수 sum 을 만드세요. 이 함수는 임의의 개수의 인수를 받아서 그 합을 계산합니다.
'''

def sum(*args):
    total=0
    for num in args:
        total += num
    return total

print(sum(10,20,30,40,50))
