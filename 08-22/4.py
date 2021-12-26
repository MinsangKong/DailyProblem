#https://www.acmicpc.net/problem/12896
#백준 12896번 스크루지 민호 (그래프 이론)
#import sys
#input = sys.stdin.readline
from collections import deque

def bfs(idx):
    visited = [-1]*(n+1)
    visited[idx] = 0
    q = deque([idx])
    while q :
        now = q.popleft()
        
        for _next in graph[now] :
            if visited[_next] == -1:
                visited[_next] = visited[now] + 1
                q.append(_next)
    
    cnt = 0
    node = 0
    for i in range(1,n+1):
        if cnt < visited[i]:
            cnt = visited[i]
            node = i
    return node, cnt

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

first, _ = bfs(1)
_, diameter = bfs(first)
print((diameter+1)//2)
'''
트리 내에서 가장 먼 노드간의 거리 -> 트리의 지름
아무 node에서 가장 먼 거리의 node를 구하고 그 node에서 트리의 지름값의 중앙이 최적의 거리가 된다.
'''