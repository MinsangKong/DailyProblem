#https://www.acmicpc.net/problem/14938
#백준 14938번 서강 그라운드 (플로이드)
#import sys
#input = sys.stdin.readline
INF = int(1e9)

n, m, r = map(int, input().split())
items = list(map(int, input().split()))
graph = [[INF]*n for _ in range(n)]

for i in range(n):
    graph[i][i] = 0
for _ in range(r):
    a,b,c = map(int, input().split())
    graph[a-1][b-1] = c
    graph[b-1][a-1] = c
    
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j :
                continue
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
            
result = 0
for i in range(n):
    total = 0
    for j in range(n):
        if graph[i][j] <= m:
            total+=items[j]
    result = max(result,total)
print(result)