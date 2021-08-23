#https://www.acmicpc.net/problem/15658
#백준 15658번 연산자 끼워넣기 (2) (BFS)
#import sys
#input = sys.stdin.readline
from collections import deque

def bfs(n):
    global minV, maxV
    q = deque()
    q.append((oper[0],oper[1],oper[2],oper[3],num[0],1))
    while q:
        plus, minus, mul, div, answer, cnt = q.popleft()
        if cnt == n:
            minV = min(answer,minV)
            maxV = max(answer,maxV)
            continue
        if plus > 0 :
            q.append((plus-1,minus,mul,div,answer+num[cnt],cnt+1))
        if minus > 0:
            q.append((plus,minus-1,mul,div,answer-num[cnt],cnt+1))
        if mul > 0 :
            q.append((plus,minus,mul-1,div,answer*num[cnt],cnt+1))
        if div > 0 :
            if answer < 0:
                a = -(-answer//num[cnt])
                q.append((plus,minus,mul,div-1,a,cnt+1))
            else:
                q.append((plus,minus,mul,div-1,answer//num[cnt],cnt+1))

n = int(input())
num = list(map(int, input().split()))
oper = list(map(int, input().split()))
minV = int(1e9)
maxV = -int(1e9)

bfs(n)

print(maxV)
print(minV)
'''
다른 사람이 작성한 코드를 보니까 DFS를 통한 백트래킹으로 풀었는데 속도 면에서 더 빨랐다.
'''