#https://www.acmicpc.net/problem/18243
#백준 18243번 Small World Network (플로이드)
import sys
#input = sys.stdin.readline
INF = int(1e9)

n, k = map(int, input().split())
if n == 1:
    print("Big World!")
    sys.exit(0)
graph = [[101]*n for _ in range(n)]

for i in range(k):
    a,b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1
    
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j :
                graph[i][j] = 0
                continue
            else:
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

flag = True
for i in range(n):
    for j in range(n):
        if graph[i][j] > 6:
            flag = False
            break
if flag:
    print("Small World!")
else:
    print("Big World!")