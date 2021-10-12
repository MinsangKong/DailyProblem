#https://www.acmicpc.net/problem/13424
#백준 13424번 비밀 모임(BFS)
import sys
#input = sys.stdin.readline
from collections import deque

def bfs(idx):
    visited = [int(1e9)]*(n+1)
    visited[idx] = 0
    q = deque()
    cnt = 0
    q.append(idx)
    while q:
        node = q.popleft()
        for nextnode, dist in graph[node]:
            if visited[nextnode] > visited[node]+dist:
                visited[nextnode] = visited[node]+dist
                q.append(nextnode)
    return visited[:]

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    
    for _ in range(m):
        a,b,c = map(int, input().split())
        graph[a].append([b,c])
        graph[b].append([a,c])
        
    k = int(input())
    friends = list(map(int, input().split()))
    
    result = sys.maxsize
    idx = 0
    distance = []
    for friend in friends:
        distance.append(bfs(friend))
        
    for i in range(1,n+1):
        total = 0
        for j in range(len(distance)):
            total += distance[j][i]
        if total < result:
            result = total
            idx = i
    print(idx)
#친구들만 BFS로 처리한 방식과 속도 차이가 없었다