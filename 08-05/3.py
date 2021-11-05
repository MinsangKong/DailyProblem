#https://www.acmicpc.net/problem/11404
#백준 11404번 플로이드 (플로이드)
#import sys
#input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF]*n for _ in range(n)]

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1],c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                graph[i][j] = 0
                continue
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
            
for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            print(0, end = " ")
        else:
            print(graph[i][j], end = " ")
    print()