#https://www.acmicpc.net/problem/11657
#백준 11657번 타임머신(밸만 포드)
#import sys
#input = sys.stdin.readline
INF = int(1e9)

def bf():
    for r in range(n): # 반복 여부 체크
        for i in range(1,n+1):
            for node,dist in graph[i]:
                if distance[i] != INF and distance[node] > distance[i]+dist:
                    distance[node] = distance[i]+dist
                    if r == n-1 : #n번째 라운드에서 값이 갱신된다면 음수 순환이 존대
                        return True
    return False
                    
    for i in range(2,n+1):
        print(-1 if distance[i] == INF else distance[i])
            
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)
distance[1] = 0

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
    
if bf():
    print(-1)
else:
    for i in distance[2:]:
        print(-1 if i == INF else i)