#https://www.acmicpc.net/problem/14284
#백준 14284번 간선 이어가기(다익스트라)
#import sys
#input = sys.stdin.readline
import heapq

def dijkstra(s,t):
    distance = [int(1e9)]*(n+1)
    distance[s] = 0
    q = []
    heapq.heappush(q,[0,s])
    while q:
        weight, now = heapq.heappop(q)
        
        if now == t:
            return weight
        
        if weight > distance[now]:
            continue
            
        for nodeNext, cost in graph[now]:
            if distance[nodeNext] > cost+weight:
                distance[nodeNext] = cost+weight
                heapq.heappush(q,[cost+weight, nodeNext])

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
    
s, t = map(int, input().split())
print(dijkstra(s,t))