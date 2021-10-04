#https://www.acmicpc.net/problem/13910
#백준 13910번 개업(BFS)
#import sys
#input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
woks = sorted(list(map(int, input().split())))

cases = set()
visited = [0]*(n+1)

for i in range(m):
    if woks[i] > n :
        break
    cases.add(woks[i])
    visited[woks[i]] = 1
    for j in range(i):
        if woks[i]+woks[j] > n:
            break
        cases.add(woks[i]+woks[j])
        visited[woks[i]+woks[j]] = 1
        
cases = sorted(cases)

q = deque(cases)

while q:
    now = q.popleft()
    
    if now == n:
        break
        
    for case in cases:
        if now + case <= n and not visited[now+case]:
            visited[now+case] = visited[now]+1
            q.append(now+case)

print(-1 if not visited[n] else visited[n])