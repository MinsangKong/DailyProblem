#https://www.acmicpc.net/problem/11403
#백준 11403번 경로 찾기(플로이드)
#import sys
#input=sys.stdin.readline
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0 and graph[i][k] == 1 and graph [k][j] == 1:
                graph[i][j] = 1

for i in graph:
    for j in i:
        print(j, end=' ')
    print()