#https://www.acmicpc.net/problem/20007
#백준 20007번 떡 돌리기 (다익스트라)
#import sys
#input = sys.stdin.readline
import heapq
INF = int(1e9)

def dijkstra(s):
    distance = [INF]*n
    distance[s] = 0
    q = []
    q.append([0,s])
    while q :
        cost, now = heapq.heappop(q)
        
        if distance[now] != cost:
            continue
        
        for node, dist in graph[now]:
            if distance[node] > cost + dist :
                distance[node] = cost + dist
                heapq.heappush(q, [cost+dist, node])
                
    cnt = 1
    cur = x
    distance.sort()
    for i in range(1,n):
        value = distance[i]
        if cur - value*2 >= 0:
            cur -= value*2
        else :
            if x >= value*2 :
                cnt += 1
                cur = x - value*2
            else:
                return -1
    return cnt

n,m,x,y = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
print(dijkstra(y)) 