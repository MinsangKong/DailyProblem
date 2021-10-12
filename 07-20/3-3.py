#https://www.acmicpc.net/problem/13424
#백준 13424번 비밀 모임(다익스트라)
#import sys
#input = sys.stdin.readline
import heapq
INF = int(1e9)

def bfs(idx):
    visited = [INF]*(n+1)
    visited[idx] = 0
    q = []
    cnt = 0
    heapq.heappush(q,[0,idx])
    while q:
        cost, now = heapq.heappop(q)
        if visited[now] < cost:
            continue
        for nextnode, dist in graph[now]:
            if visited[nextnode] > cost+dist:
                visited[nextnode] = cost+dist
                heapq.heappush(q,[cost+dist,nextnode])
                
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
'''
추가적인 방문처리가 없기 때문에 BFS보다 dijkstra방식이 훨씬 빨랐다.
걍 다음부턴 거리문제는 무조건 dijkstra방식으로 처리하는게 좋겠다.
'''