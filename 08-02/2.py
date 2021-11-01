#https://www.acmicpc.net/problem/5972
#백준 5972번 택배 배송 (다익스트라)
#import sys
#input = sys.stdin.readline
import heapq
INF = int(1e9)

def dijkstra():
    q = []
    distance = [INF]*(n+1)
    distance[1] = 0
    q.append([0,1])
    while q :
        dist, now = heapq.heappop(q)
        
        if dist > distance[now]:
            continue
            
        for _next,cost in graph[now]:
            total = cost+dist
            if distance[_next] > total:
                distance[_next] = total
                heapq.heappush(q, [total,_next])
                
    return distance[n]

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
    
print(dijkstra())