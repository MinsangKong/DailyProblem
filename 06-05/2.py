#https://www.acmicpc.net/problem/4963
#백준 4963번 섬의 개수(BFS)
#import sys
#input = sys.stdin.readline
from collections import deque

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    
    while q :
        dx, dy = q.popleft()
        for a, b in direction:
            nx = a+dx
            ny = b+dy
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            elif visited[nx][ny] == 0 and board[nx][ny] == 1:
                q.append((nx,ny))
                visited[nx][ny] = 1
    
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
        
    board = []
    for i in range(h):
        board.append(list(map(int, input().split())))
        
    direction = [(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(1,1),(-1,1),(1,-1)]
    
    visited = [[0]*w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] == 1 and visited[i][j] == 0:
                bfs(i,j)
                cnt+=1
    print(cnt)