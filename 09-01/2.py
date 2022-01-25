#https://www.acmicpc.net/problem/15900
#백준 15900번 나무 탈출 (DFS, 그리디)
#import sys
#input = sys.stdin.readline

def dfs():
    q = [[1,0]]
    visited = [0]*(n+1)
    visited[1] = 1
    total = 0
    while q :
        now, cnt = q.pop()
        
        if now == 1 or len(graph[now]) > 1 :
            for _next in graph[now]:
                if not visited[_next]:
                    visited[_next] = 1
                    q.append([_next,cnt+1])
        else:
            total += cnt
    return total

n = int(input())
graph = [[] for _ in range(n+1)]
leaf = []

for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
dist = dfs()
if dist%2 :
    print("Yes")
else:
    print("No")