#https://www.acmicpc.net/problem/16118
#백준 16118번 달빛 여우(크루스컬)
#import sys
#input = sys.stdin.readline
import heapq
INF = int(1e9)

def fox(target):
    distance = [INF]*n
    distance[0] = 0
    q = []
    heapq.heappush(q, [0,0])
    num = INF
    while q:
        dist, now = heapq.heappop(q)
        if now == target:
            return dist
        if dist > distance[now]:
            continue
        
        for i in graph[now]:
            cost = i[0]+dist
            if distance[i[1]] > cost:
                distance[i[1]] = cost
                heapq.heappush(q,[cost,i[1]])
    return num
                
def wolf(target):
    distance = [[INF]*2 for _ in range(n)]
    distance[0][0] = 0
    distance[0][1] = 0
    q = []
    num = INF
    heapq.heappush(q, [0,0,1]) #1이면 속도 2배 0이면 속도 1/2배
    while q:
        dist, now, state = heapq.heappop(q)
        if now == target:
            return dist
        if state == 1:
            if dist > distance[now][0] :
                continue
        else:
            if dist > distance[now][1] :
                continue
        for i in graph[now]:
            if state == 1:
                cost = i[0]/2+dist
                if distance[i[1]][1] > cost:
                    distance[i[1]][1] = cost
                    heapq.heappush(q,[cost,i[1],0])
            else:
                cost = i[0]*2+dist
                if distance[i[1]][0] > cost:
                    distance[i[1]][0] = cost
                    heapq.heappush(q,[cost,i[1],1])
    return num

n,m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a-1].append([c,b-1])
    graph[b-1].append([c,a-1])
    
result = 0
for i in range(1,n):
    distWolf = wolf(i)
    distFox = fox(i)
    if distFox < distWolf:
        result+=1
        
print(result)

'''
알고리즘 자체는 맞는 거 같은데 시간초과를 어떻게 해결해야 할 지 모르겠다.
문제 채점 기준 범위가 너무 좁아서 통과한 사람이 매우 적다.
정답 알고리즘과 거의 근접하지만 여러번의 다익스트라 없이 반환할 때 리스트를 반환했으면
두 번의 다익스트라로 해결 할 수 있었다.
'''