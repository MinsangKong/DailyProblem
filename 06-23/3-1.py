#https://www.acmicpc.net/problem/5567
#백준 5567번 결혼식(플로이드)
#import sys
#input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i == j:
                continue
            if graph[i][j] == 0 and graph[i][k] >= 1 and graph[k][j] >= 1:
                graph[i][j] = max(graph[i][k],graph[k][j])+1
cnt = 0

for i in range(2,n+1):
    if graph[1][i] == 1 or graph[1][i] == 2:
        cnt+=1
print(cnt)
'''
플로이드를 활용한 방법은 중간에 틀림...
'''