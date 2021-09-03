#https://www.acmicpc.net/problem/11724
#백준 11724번 연결 요소의 개수(dfs)
import sys
#input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(v):
    visited[v] = 1
    for i in range(1, n+1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i)


n, m = map(int, input().split())
graph = [[0] * (n+1) for i in range(n+1)]
visited = [0] * (n+1)

for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1
    graph[v2][v1] = 1

count = 0
for i in range(1, n+1):
    if visited[i] == 0:
        dfs(i)
        count += 1
print(count)