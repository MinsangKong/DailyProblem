#https://www.acmicpc.net/problem/16988
#백준 16988번 Baaaaaaaaaduk2 (Easy) (그래프이론)
#import sys
#input = sys.stdin.readline
from collections import deque

def scoring():
    cnt = 0
    visited = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and board[i][j] == 2:
                cnt += bfs(i,j,visited)
    return cnt

def bfs(x,y,visited):
    visited[x][y] = 1
    q = deque()
    q.append([x,y])
    cnt = 1
    flag = True
    while q :
        dx, dy = q.popleft()
        
        for a,b in direction:
            nx = dx+a
            ny = dy+b
            if 0 <= nx < n and 0 <= ny < m :
                if not board[nx][ny] :
                    flag = False
                elif not visited[nx][ny] and board[nx][ny] == 2:
                    cnt += 1
                    visited[nx][ny] =1
                    q.append([nx,ny])
    return cnt if flag else 0

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
result = 0
cases = []
direction = [(1,0),(0,1),(-1,0),(0,-1)]

for i in range(n):
    for j in range(m):
        if not board[i][j]:
            cases.append([i,j])
            
length = len(cases)
for i in range(length-1):
    for j in range(i+1,length):
        sx, sy = cases[i]
        ex, ey = cases[j]
        board[sx][sy] = 1
        board[ex][ey] = 1
        stones = scoring()
        if result < stones :
            result = stones
        board[sx][sy] = 0
        board[ex][ey] = 0
        
print(result)