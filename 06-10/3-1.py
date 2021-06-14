#https://www.acmicpc.net/problem/13023
#백준 13023번 ABCDE(DFS, 백트래킹)
import sys
#input =sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(node,cnt):
    global result
    if cnt >= 5:
        result =True
        return 
    else:
        for i in graph[node]:
            if visited[i] == 0:
                visited[i] = 1
                dfs(i,cnt+1)
                visited[i] = 0
n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
result = False
for i in range(n):
    visited = [0]*n
    visited[i] = 1
    if result :
        break
    else:
        dfs(i,1)
        
if result:
    print(1)
else:
    print(0)
    
'''
visited 배열을 재사용하는 것보다 visited 배열을 새로 구현하는 방식이 더 빨랐다.
'''