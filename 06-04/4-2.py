#https://www.acmicpc.net/problem/16118
#백준 16118번 달빛 여우(크루스컬)
#import sys
#input = sys.stdin.readline
import heapq
INF = int(1e9)

def fox():
    distance = [INF]*n
    distance[0] = 0
    q = []
    heapq.heappush(q, [0,0])
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        
        for i in graph[now]:
            cost = i[0]+dist
            if distance[i[1]] > cost:
                distance[i[1]] = cost
                heapq.heappush(q,[cost,i[1]])
    return distance

def wolf():
    distance = [[INF]*n for _ in range(2)]
    distance[1][0] = 0
    q = []
    heapq.heappush(q, [0,0,0])
    while q:
        dist, now, state = heapq.heappop(q)
        if state and distance[0][now] < dist:
            continue
        elif not state and distance[1][now] < dist:
            continue
                    
        for i in graph[now]:
            if state:
                cost = dist+(i[0]*2)
                if cost < distance[1][i[1]]:
                    distance[1][i[1]] = cost
                    heapq.heappush(q,[distance[1][i[1]],i[1],0])
            else:
                cost = dist+(i[0]//2)
                if cost < distance[0][i[1]]:
                    distance[0][i[1]] = cost
                    heapq.heappush(q,[distance[0][i[1]],i[1],1])
    return distance

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a-1].append([c*2,b-1])
    graph[b-1].append([c*2,a-1])
    
distFox = fox() 
distWolf = wolf()

result = 0

for i in range(n):
    if distFox[i] < min(distWolf[0][i], distWolf[1][i]):
        result += 1
print(result)
'''
답 자체는 맞았지만 서버 상황에 따라서 정답이 결정되는 거지같은 문제.
아래의 해답과 알고리즘 자체는 똑같지만 heapq, 변수 범위 차이에서 발생하는 약간의 
속도차이로 정답여부가 결정된다.
'''