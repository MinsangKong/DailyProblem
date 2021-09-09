#https://www.acmicpc.net/problem/17086
#백준 17086번 아기 상어 2 (BFS)
#import sys
#input = sys.stdin.readline
from collections import deque
INF = int(1e9)

def bfs():
    visited = [[INF]*m for _ in range(n)]
    q = deque()
    for a,b in sharks:
        q.append((a,b))
        visited[a][b] = 0
    while q:
        x, y = q.popleft()
        
        for a,b in direction:
            nx = x+a
            ny = y+b
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] > visited[x][y]+1 :
                    visited[nx][ny] = visited[x][y]+1
                    q.append((nx,ny))
    #print(visited)
    return max(map(max, visited))

n, m = map(int, input().split())

board = [[0]*m for _ in range(n)]
sharks = []

direction = [(1,0),(-1,0),(0,1),(0,-1),(1,-1),(-1,1),(-1,-1),(1,1)]

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(m):
        if data[j] == 1:
            sharks.append((i,j))
            board[i][j] = 1
    
print(bfs())