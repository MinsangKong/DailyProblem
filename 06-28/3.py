#https://www.acmicpc.net/problem/12931
#백준 12931번 두 배 더하기(그리디)
#import sys
#input = sys.stdin.readline

n = int(input())

cnt = 0
b = list(map(int, input().split()))

while True:
    flag = False
    for i in range(n):
        if b[i] == 0:
            continue
        elif b[i] == 1:
            cnt+=1
            b[i]-=1
        elif b[i] % 2 != 0:
            b[i]-=1
            cnt+=1
            flag = True
        else:
            flag = True
        b[i]//=2
    if flag:
        cnt+=1
    if sum(b) == 0:
        print(cnt)
        break