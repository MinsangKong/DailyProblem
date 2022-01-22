#https://www.acmicpc.net/problem/14442
#백준 14442번 벽 부수고 이동하기 2 (BFS)
#import sys
#input = sys.stdin.readline
from collections import deque
INF = int(1e9)

def bfs():
    visited = [[[INF]*m for _ in range(n)] for _ in range(k+1)]
    visited[k][0][0] = 1
    q = deque([[k,0,0]])
    while q :
        cnt, x, y = q.popleft()
        #print(cnt,x,y)
        if (x,y) == (n-1,m-1):
            return visited[cnt][x][y]
        
        for a,b in direction :
            nx = x+a
            ny = y+b
            if nx < 0 or nx >= n or ny < 0 or ny >= m :
                continue
            if board[nx][ny] :
                if cnt >= 1 and visited[cnt-1][nx][ny] == INF:
                    visited[cnt-1][nx][ny] = visited[cnt][x][y]+1
                    q.append([cnt-1,nx,ny])
            else:
                if visited[cnt][nx][ny] == INF:
                    visited[cnt][nx][ny] = visited[cnt][x][y]+1
                    q.append([cnt,nx,ny])
                    
    return -1

n,m,k = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]
direction = [(0,1),(1,0),(0,-1),(-1,0)]

print(bfs())