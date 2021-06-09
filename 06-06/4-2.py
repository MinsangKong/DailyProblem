#https://www.acmicpc.net/problem/20183
#백준 20183번 골목대장 호석-효율성2(이분탐색,다익스트라)
#import sys
#input = sys.stdin.readline
import heapq
INF = int(1e9)

def dijkstra(limit):
    dist = [float('inf')] * (n+1)
    dist[s] = 0
    H = [(0, s)]
    while H:
        d, u = heapq.heappop(H)
        if dist[u] != d:
            continue
        for v, cc in graph[u]:
            if cc>limit: continue
            if dist[v] > d + cc:
                dist[v] = d + cc
                heapq.heappush(H, (d + cc, v))
    return dist[e]<=total
        
n, m, s, e, total = map(int, input().split())
graph = [[] for _ in range(n+1)]


costs = set()
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
    costs.add(c)
    
costs = sorted(costs)
l = 0
r = len(costs)

while l<r:
    m = (l+r)//2
    if dijkstra(costs[m]): r=m
    else: l=m+1
print(costs[l] if l<len(costs) else -1)

'''

'''