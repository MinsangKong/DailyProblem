#https://www.acmicpc.net/problem/13424
#백준 13424번 비밀 모임(BFS)
#import sys
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
                
    for friend in friends:
        cnt += visited[friend]
    return cnt

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
    
    result = int(1e9)
    idx = 0
    
    for i in range(1,n+1):
        num = bfs(i)
        if result > num :
            result = num
            idx = i
    print(idx)
#제출하고 보니 더 좋은 생각이 떠올랐다. 친구들만 BFS문을 처리하면 더 빠를 수 있을것 같다
#빠르게 작성한 사람들을 보면 다 heapq로 처리했다. 불필요한 방문처리가 없어서 빠른걸까?