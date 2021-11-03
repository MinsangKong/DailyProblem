#https://www.acmicpc.net/problem/15681
#백준 15681번 트리와 쿼리 (DFS)
import sys
#input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(idx):
    visited[idx] = 1
    for _next in graph[idx]:
        if not visited[_next]:
            result[idx] += dfs(_next)
    return result[idx]

n, r, q = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
for _ in range(n-1):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
result = [1]*(n+1)
dfs(r)
for _ in range(q):
    num = int(input())
    print(result[num])