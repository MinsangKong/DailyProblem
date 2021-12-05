#https://www.acmicpc.net/problem/9372
#백준 9372번 상근이의 여행 (BFS)
#import sys
#input = sys.stdin.readline
from collections import deque

def bfs(x):
    q = deque()
    q.append(x)
    check[x] = 1
    count = 0
    while q:
        x = q.popleft()
        for nx in arr[x]:
            if check[nx] == 0:
                check[nx] = 1
                count += 1
                q.append(nx)
    return count

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = [[] for _ in range(n+1)]
    check = [0 for _ in range(n+1)]
    for _ in range(m):
        x, y = map(int, input().split())
        arr[x].append(y)
        arr[y].append(x)
        
    cnt = 0
    for i in range(1,n+1):
        if check[i] == 0:
            cnt += bfs(i)
    print(cnt)