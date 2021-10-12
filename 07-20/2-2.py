#https://www.acmicpc.net/problem/1240
#백준 1240번 노드사이의 거리(DFS)
import sys
#input = sys.stdin.readline

def dfs(idx,target,total):
    q = [[idx,total]]
    while q:
        now, cost = q.pop()
        if now == target:
            return cost
        for node,dist in graph[now]:
            if not visited[node] :
                visited[node] = 1
                q.append([node,cost+dist])

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

for _ in range(m):
    visited = [0]*(n+1)
    a,b = map(int, input().split())
    visited[a] = 1
    print(dfs(a,b,0))
'''
당연히 모든 움직임을 계산한 뒤에 출력만 하는 방식이 더 빠를 줄 알았는데
여기서는 반복된 입력이 없어서 그런지 매번 입력을 처리해주는 방식이 더 빨랐다.
'''