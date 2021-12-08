#https://www.acmicpc.net/problem/11562
#백준 11562번 백양로 브레이크 (플로이드)
#import sys
#input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, (input().split()))
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    u, v, b = map(int, input().split())
    graph[u][v] = 0
    if b == 0:
        graph[v][u] = 1
    else:
        graph[v][u] = 0

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                graph[a][b] = 0
                continue
            if graph[a][b] > graph[a][k] + graph[k][b]:
                graph[a][b] = graph[a][k] + graph[k][b]

k = int(input())
for i in range(k):
    s, e = map(int, input().split())
    print(graph[s][e])