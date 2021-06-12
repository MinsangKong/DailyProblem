#https://www.acmicpc.net/problem/14699
#백준 14699번 관악산 등산(위상정렬)
#import sys
#input = sys.stdin.readline
from collections import deque

n,m = map(int, input().split())

heights = list(map(int, input().split()))
indegree = [0]*n

graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    if heights[a-1] > heights[b-1]:
        indegree[b-1]+=1
    else:
        indegree[a-1]+=1
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
    
result = [1]*n

q = deque()
for i in range(n):
    if indegree[i] == 0:
        q.append(i)
        
print(indegree)
while q:
    now = q.popleft()
    
    for i in graph[now]:
        indegree[i]-=1
        if indegree[i] == 0:
            result[i]+=result[now]
            q.append(i)
        
for i in result:
    print(i)
    
'''
높이 순서대로 위상 정렬을 실시해야 시간 초과가 발생X
'''