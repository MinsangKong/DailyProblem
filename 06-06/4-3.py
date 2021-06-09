#https://www.acmicpc.net/problem/20168
#백준 20168번 골목대장 호석(다익스트라, 이분탐색)
#import sys
#input = sys.stdin.readline
import heapq
INF = int(1e9)

def dijkstra(a,b,c,mid):
    q = []
    distance = [INF]*n
    distance[a] = 0
    heapq.heappush(q,[0,a])
    while q:
        dist, now = heapq.heappop(q)
        if  -dist > distance[now]:
            continue
        if now == b:
            return distance[b] <= c
            
        for nextnode,nextdist in graph[now]:
            cost = nextdist+distance[now]
            if cost > c or nextdist > mid:
                continue
            if cost < distance[nextnode]:
                distance[nextnode] = cost
                heapq.heappush(q, [-cost,nextnode])
    return False
        
n, m, s, e, total = map(int, input().split())
graph = [[] for _ in range(n)]

left = INF
right = -INF

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a-1].append([b-1,c])
    graph[b-1].append([a-1,c])
    left = min(left,c)
    right = max(right,c)
    
result = -1

while left <= right:
    mid = (left+right)//2
    if dijkstra(s-1,e-1,total,mid):
        result = mid
        right = mid-1
    else:
        left = mid+1
        
print(result)
'''
다익스트라를 적용할 때
'''