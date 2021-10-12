#https://www.acmicpc.net/problem/1240
#백준 1240번 노드사이의 거리(DFS)
import sys
#input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(idx,target,total):
    for node,dist in graph[target]:
        if not visited[node] :
            cost = dist + total
            visited[node] = 1
            distance[idx][node] = cost
            dfs(idx,node,cost)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
    
distance = [[0]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    visited = [0]*(n+1)
    visited[i] = 1
    dfs(i,i,0)
    
#print(distance)
for _ in range(m):
    a,b = map(int, input().split())
    print(distance[a][b])