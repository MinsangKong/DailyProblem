#https://www.acmicpc.net/problem/20182
#백준 20182번 골목 대장 호석(다익스트라, 시간 복잡도)
#import sys
#input = sys.stdin.readline
import heapq
INF = int(1e9)

def dijkstra(limit):
    distance = [INF] *(n+1)
    distance[a] = 0
    q = []
    heapq.heappush(q, (0, a))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] != dist:
            continue
        for node, cost in graph[now]:
            if cost > limit:
                continue
            if distance[node] > dist+cost:
                distance[node] = dist+cost
                heapq.heappush(q, (dist+cost,node))
    return distance[b] <= c

n, m, a, b, c = map(int, input().split())
graph = [[] for _ in range(n+1)]

costs = set()
for _ in range(m):
    s, e, cost = map(int, input().split())
    graph[s].append([e,cost])
    graph[e].append([s,cost])
    costs.add(cost)
    
costs = sorted(costs)

l = 0
r = len(costs)
result = 0

while l <= r:
    mid = (l+r)//2
    if mid >= len(costs):
        result = mid
        break
    if dijkstra(costs[mid]) :
        r = mid-1
        result = mid
    else:
        l = mid+1
        
print(costs[result] if result < len(costs) else -1)
'''
효율성 1 테스트에서는 result로 처리하는 방식은 맞았지만
효율성 2 테스트에서는 c의 범주가 달랐기 때문에 int(1e9)가 아닌 float('inf')로 해야
정답으로 처리됐다... 파이썬에서는 항상 범위를 염두하지 않았기 때문에 계속 몰랐다.
1e9 = 10의 9제곱 (1,000,000,000) 
즉 , 10억이기 때문에 10억보다 큰 수는 float('inf') 나 sys.maxsize로 처리해줘야한다.
'''