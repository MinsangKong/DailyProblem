#https://www.acmicpc.net/problem/13911
#백준 13911번 집 구하기(다익스트라)
import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)

def dijkstra(start, nodeList):
    q = []
    heapq.heappush(q, (0,start))
    while q:
        dist, now = heapq.heappop(q)
        if nodeList[now] < dist:
            continue
        for i in graph[now]:
            if i[0] == v+1 or i[0] == v+2:
                continue
            cost = dist+i[1]
            if cost < nodeList[i[0]]:
                nodeList[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))
v,e = map(int, input().split())
graph = [[] for _ in range(v+3)]
mLimit = v+1
sLimit = v+2
l = []

for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
    
m,x = map(int, input().split())
macs = list(map(int, input().split()))
s, y = map(int, input().split())
stars = list(map(int, input().split()))

for m in macs:
    graph[mLimit].append([m,0])
    graph[m].append([mLimit,0])
for s in stars:
    graph[sLimit].append([s,0])
    graph[s].append([sLimit,0])

mNodeList=[INF for i in range(v+3)]
mNodeList[v+1]=0

sNodeList=[INF for i in range(v+3)]
sNodeList[v+2]=0

dijkstra(v+1, mNodeList)
dijkstra(v+2, sNodeList)

result = INF

for i in range(1,v+1):
    if i in macs or i in stars:
        continue
    if mNodeList[i] <= x and sNodeList[i] <= y:
        if mNodeList[i]+sNodeList[i] < result:
            result = mNodeList[i]+sNodeList[i]
            
if result != INF:
    print(result)
else:
    print(-1)