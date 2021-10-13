#https://www.acmicpc.net/problem/4096
#백준 4096번 팰린드로미터(문자열)
#import sys
#input = sys.stdin.readline

def check(num):
    for i in range(length//2):
        if num[i] != num[len(num)-(1+i)]:
            return False
    return True

while True:
    data = input().rstrip()
    cnt = 0
    length = len(data)
    if data == '0':
        break
    if check(data):
        print(0)
        continue
    num = int(data)
    while True:
        num += 1
        cnt += 1
        temp = str(num)
        num = '0'*(length-len(temp))+temp
        if check(num):
            print(cnt)
            break
        else:
            num = int(num)
'''
앞의 문자열을 채울 때 별도의 함수가 존재했다.
1)"".zfill(width) -> "2".zfill(3) -> "002" 
zifil을 사용하면 width까지 '0'으로 가득 채울 수 있다
2)"".rjust(width, [fillchar]) -> "2".rjust(3, "0") -> "002"
zifil과 유사하지만 채워지는 문자를 지정할 수 있다.
'''