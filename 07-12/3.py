#https://www.acmicpc.net/problem/14567
#백준 14567번 선수과목(위상정렬)
#import sys
#input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
indegree = [0]*n
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    indegree[b-1] += 1
    
result = [0]*n

q = deque()

for i in range(n):
    if not indegree[i]:
        q.append([i, 1])
        
while q:
    now, cnt = q.popleft()
    
    result[now] = cnt
    
    for node in graph[now]:
        indegree[node] -= 1
        if not indegree[node]:
            q.append([node, cnt+1])
            
print(*result)