#https://www.acmicpc.net/problem/2211
#백준 2211번 네트워크 복구(다익스트라)
#import sys
#input = sys.stdin.readline
import heapq
INF = int(1e9)

def dijkstra():
    distance = [INF]*(n+1)
    distance[1] = 0
    q = []
    q.append([0,1])
    way = dict()
    while q:
        dist, now = heapq.heappop(q)
        
        if dist > distance[now] :
            continue
            
        for _next,cost in graph[now]:
            if distance[_next] > cost+dist:
                way[_next] = now
                distance[_next] = cost+dist
                heapq.heappush(q,[cost+dist,_next])
                
    print(len(way))
    for key in way:
        print(key, way[key])
        
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

dijkstra()