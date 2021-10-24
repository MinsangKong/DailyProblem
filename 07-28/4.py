#https://www.acmicpc.net/problem/2252
#백준 2252번 줄세우기 (위상정렬)
#import sys
#input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
indegree = [0]*(n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
    
q = deque()
result = []

for i in range(1,n+1):
    if not indegree[i]:
        q.append(i)
        result.append(i)
        

while q :
    now = q.popleft()
    
    for target in graph[now]:
        indegree[target] -= 1
        if not indegree[target] :
            result.append(target)
            q.append(target)

print(*result)