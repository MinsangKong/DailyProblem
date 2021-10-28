#https://www.acmicpc.net/problem/14940
#백준 14940번 쉬운 최단거리 (BFS)
#import sys
#input = sys.stdin.readline
from collections import deque

def bfs(x,y):
    q = deque()
    q.append([x,y])
    while q:
        dx, dy = q.popleft()
        
        for a,b in direction:
            nx = dx+a
            ny = dy+b
            if 0 <= nx < n and 0 <= ny < m :
                if board[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = visited[dx][dy]+1
                    q.append([nx,ny])

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
direction = [(1,0),(-1,0),(0,1),(0,-1)]

for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            bfs(i,j)
            
for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and not visited[i][j]:
            visited[i][j] = -1
for i in visited:
    print(*i)