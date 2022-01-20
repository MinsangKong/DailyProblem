#https://www.acmicpc.net/problem/14923
#백준 14923번 미로 탈출 (BFS)
#import sys
#input = sys.stdin.readline
from collections import deque
INF = int(1e9)

def bfs(hx,hy):
    visited = [[[INF]*m for _ in range(n)] for _ in range(2)]
    visited[0][hx][hy] = 0
    q = deque([[0,hx,hy]])
    while q :
        staff, x, y = q.popleft()
        #print(staff,x,y)
        if x == ex-1 and y == ey-1 :
            return visited[staff][x][y]
        for a,b in direction:
            nx = x+a
            ny = y+b
            if nx < 0 or nx >= n or ny < 0 or ny >= m :
                continue
            if not board[nx][ny] :
                if visited[staff][nx][ny] == INF:
                    visited[staff][nx][ny] = visited[staff][x][y]+1
                    q.append([staff,nx,ny])
            else:
                if not staff and visited[1][nx][ny] == INF:
                    visited[1][nx][ny] = visited[0][x][y]+1
                    q.append([1,nx,ny])
    return -1      

n,m = map(int, input().split())
hx, hy = map(int, input().split())
ex, ey = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
direction = [(0,1),(1,0),(0,-1),(-1,0)]

print(bfs(hx-1,hy-1))