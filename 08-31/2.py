#https://www.acmicpc.net/problem/18352
#백준 18352번 특정 거리의 도시 찾기 (BFS)
#import sys
#input = sys.stdin.readline
from collections import deque

def bfs(idx):
    q = deque([idx])
    while q:
        n= q.popleft()
        for j in road[n]:
            if result[j] == -1:
                result[j]=result[n]+1
                q.append(j)
                
n, m, k, x = map(int, input().split())
road = [[] for _ in range(n)]
result = [-1]*n
result[x-1] = 0
for i in range(m):
    a, b = map(int, input().split())
    road[a-1].append(b-1)
    
bfs(x-1)

if k not in result:
    print(-1)
else:
    for i in range(n):
        if result[i] == k:
            print(i+1)