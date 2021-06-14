#https://www.acmicpc.net/problem/13023
#백준 13023번 ABCDE(DFS, 백트래킹)
import sys
#input =sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(node,cnt):
    global result
    visited[node] = 1
    if cnt == 5:
        result =True
        return 
    for i in graph[node]:
        if visited[i] == 0:
            dfs(i,cnt+1)
            visited[i] = 0

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
result = False
visited = [0]*n
for i in range(n):
    dfs(i,1)
    visited[i] = 0
    if result :
        break
        
if result:
    print(1)
else:
    print(0)