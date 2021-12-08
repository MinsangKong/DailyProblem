#https://www.acmicpc.net/problem/11562
#백준 11562번 백양로 브레이크 (다익스트라)
#import sys
#input = sys.stdin.readline
import heapq
INF = int(1e9)

def dijkstra(s):
    visited = [INF]*(n+1)
    visited[s] = 0
    q = [[0,s]]
    while q:
        cnt, now = heapq.heappop(q)
        if visited[now] < cnt :
            continue
        for _next,state in graph[now]:
            if visited[_next] > cnt+state :
                visited[_next] = cnt+state
                heapq.heappush(q,[cnt+state,_next])
                
    return visited

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u,v,b = map(int, input().split())
    if b :
        graph[u].append([v,0])
        graph[v].append([u,0])
    else:
        graph[u].append([v,0])
        graph[v].append([u,1])
        
dist = [[-1]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    dist[i] = dijkstra(i)
queries = int(input())
for _ in range(queries):
    s, e = map(int, input().split())
    print(dist[s][e])