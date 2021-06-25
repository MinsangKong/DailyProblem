#https://www.acmicpc.net/problem/20152
#백준 20152번 Game Addiction(BFS,그리디)
#import sys
#input = sys.stdin.readline
from collections import deque

def bfs(x,y):
    q = deque()
    visited[x][x] = 0
    q.append((0,x,x))
    while q:
        dist, dx, dy = q.popleft()
        if dx > y or dy > y :
            continue
        for a,b in direction:
            nx = dx+a
            ny = dy+b
            if 0 <= nx < 31 and 0 <= ny < 31:
                if visited[nx][ny] == -1 and nx >= ny:
                    q.append([dist+1,nx,ny])
                    visited[nx][ny] = dist+1
                    graph[nx][ny]+=graph[dx][dy]
                elif visited[nx][ny] == dist+1:
                    graph[nx][ny]+=graph[dx][dy]
h, t = map(int, input().split())

graph = [[0]*31 for _ in range(31)]
visited = [[-1]*31 for _ in range(31)]

start = min(h,t)
end = max(h,t)
graph[start][start] = 1
direction = [(1,0),(-1,0),(0,1),(0,-1)]

bfs(start,end)

print(graph[end][end])