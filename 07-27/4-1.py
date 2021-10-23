#https://www.acmicpc.net/problem/2307
#백준 2307번 도로검문 (다익스트라)
#import sys
#input = sys.stdin.readline
import heapq
INF = int(1e9)

def dijkstra():
    q = []
    distance = [INF]*(n+1)
    distance[1] = 0
    q.append([0,1,[1]])
    total = 0
    way = []
    delayed = 0
    while q :
        dist, now, direction = heapq.heappop(q)
        if now == n :
            way = direction
            total = dist
            break
        if distance[now] != dist :
            continue
        for target,time in node[now]:
            if distance[target] > dist+time :
                distance[target] = dist+time
                heapq.heappush(q, [dist+time,target,direction+[target]])
    for i in range(1,len(way)):
        num = find([way[i],way[i-1]])
        if num == -1 :
            return -1
        delayed = max(num,delayed)
    return delayed-total

def find(limit):
    q = []
    distance = [INF]*(n+1)
    distance[1] = 0
    q.append([0,1])
    while q :
        dist, now = heapq.heappop(q)
        if now == n :
            return dist
        if distance[now] != dist :
            continue
            
        for target,time in node[now]:
            if target in limit and now in limit:
                continue
            if distance[target] > dist+time :
                distance[target] = dist+time
                heapq.heappush(q, [dist+time,target])
    return -1

n, m = map(int ,input().split())
node = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,t = map(int, input().split())
    node[a].append([b,t])
    node[b].append([a,t])
    
print(dijkstra())