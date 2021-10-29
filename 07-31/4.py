#https://www.acmicpc.net/problem/1766
#백준 1766번 문제집 (위상정렬)
#import sys
#input = sys.stdin.readline
import heapq

n, m = map(int, input().split())
indegree = [0]*(n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
    
q = []
result = []

for i in range(1,n+1):
    if not indegree[i]:
        heapq.heappush(q,i)
        
while q : 
    now = heapq.heappop(q)
    result.append(now)
    for node in graph[now]:
        indegree[node] -= 1
        if not indegree[node] :
            heapq.heappush(q,node)
            
print(*result)