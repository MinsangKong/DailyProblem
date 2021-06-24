#https://www.acmicpc.net/problem/7562
#백준 7562번 나이트의 이동(BFS)
#import sys
#input = sys.stdin.readline
from collections import deque
def bfs(x,y):
    q = deque()
    q.append((x,y))
    board[x][y]=0
    while q:
        dx, dy = q.popleft()
        for a, b in direction:
            nx = a+dx
            ny = b+dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            elif board[nx][ny] > board[dx][dy]+1:
                board[nx][ny]=board[dx][dy]+1
                if nx == x_e and ny == y_e:
                    return
                q.append((nx,ny))
                
    return

t = int(input())
for _ in range(t):
    n = int(input())
    x_s, y_s = map(int, input().split())
    x_e, y_e = map(int, input().split())
    
    board = [[int(1e9)]*n for _ in range(n)]
    direction = [(1,2),(2,1),(-1,2),(1,-2),(-1,-2),(-2,-1),(-2,1),(2,-1)]
    
    bfs(x_s, y_s)
    
    print(board[x_e][y_e])