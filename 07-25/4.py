#https://www.acmicpc.net/problem/2623
#백준 2623번 음악 프로그램(위상정렬)
#import sys
#input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)

for _ in range(m):
    data = list(map(int, input().split()))
    num = data[0]
    for i in range(1,num):
        graph[data[i]].append(data[i+1])
        indegree[data[i+1]] += 1
        
q = deque()
result = []

for i in range(1,n+1):
    if not indegree[i]:
        q.append(i)
        result.append(i)
        
while q :
    now = q.popleft()
    
    for node in graph[now]:
        indegree[node] -= 1
        if indegree[node] == 0 :
            q.append(node)
            result.append(node)
            
if len(result) == n :
    for singer in result:
        print(singer)
else:
    print(0)