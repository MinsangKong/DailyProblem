#https://www.acmicpc.net/problem/14496
#백준 14496번 그대, 그머가 되어(다익스트라)
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

a, b = map(int, input().split())
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append((1, y))
    graph[y].append((1, x))

INF = sys.maxsize
dist = [INF] * (N + 1)
heap = [(0, a)]
dist[a] = 0
while heap:
    cost, u = heappop(heap)
    if dist[u] < cost:
        continue
    for w, v in graph[u]: #경로와 node를 따로 해야 listerror가 발생 안함
        next_cost = w+cost
        if dist[v] > next_cost:
            dist[v] = next_cost
            heappush(heap, (next_cost, v))
if dist[b] == INF:
    print(-1)
else:
    print(dist[b])