#https://www.acmicpc.net/problem/5567
#백준 5567번 결혼식(DFS)
#import sys
#input = sys.stdin.readline

def dfs(node, depth):
    global cnt
    if depth >= 3:
        return
    for i in graph[node]:
        if visited[i] == 0:
            visited[i] = 1
            cnt+=1
            dfs(i,depth+1)

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
visited[1] = 1
dfs(1,1)

print(cnt)