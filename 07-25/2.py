#https://www.acmicpc.net/problem/14888
#백준 14888번 연산자 끼워넣기 (BFS)
#import sys
#input = sys.stdin.readline
from collections import deque

def bfs(length):
    minV = float('inf')
    maxV = float('-inf')
    q = deque()
    q.append((oper[0],oper[1],oper[2],oper[3],num[0],1))
    while q:
        plus, minus, mul, div, n, cnt = q.popleft()
        if cnt == length:
            minV = n if n < minV else minV
            maxV = n if n > maxV else maxV
        if plus > 0 :
            q.append((plus-1,minus,mul,div,n+num[cnt],cnt+1))
        if minus > 0:
            q.append((plus,minus-1,mul,div,n-num[cnt],cnt+1))
        if mul > 0 :
            q.append((plus,minus,mul-1,div,n*num[cnt],cnt+1))
        if div > 0 :
            if n < 0:
                a = -(-n//num[cnt])
                q.append((plus,minus,mul,div-1,a,cnt+1))
            else:
                q.append((plus,minus,mul,div-1,n//num[cnt],cnt+1))
    return (maxV,minV)

n = int(input())
num = list(map(int, input().split()))
oper = list(map(int, input().split()))
length = len(num)

print(*bfs(length))