#https://www.acmicpc.net/problem/18223
#백준 18223번 민준이와 마산 그리고 건우 (다익스트라)
#import sys
#input = sys.stdin.readline
import heapq
INF = int(1e9)

def dijkstra(idx):
    distance = [INF]*(v+1)
    distance[idx] = 0
    q = [[0, idx]]
    while q :
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
            
        for _next, cost in graph[now]:
            if distance[_next] > cost+dist:
                distance[_next] = cost+dist
                heapq.heappush(q, [cost+dist, _next])
    return distance

v,e,p = map(int, input().split())
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
minjun = dijkstra(1)
kunwoo = dijkstra(p)
if minjun[v] == minjun[p]+kunwoo[v]:
    print("SAVE HIM")
else:
    print("GOOD BYE")