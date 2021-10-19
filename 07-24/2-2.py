#https://www.acmicpc.net/problem/11048
#백준 11048번 이동하기 (BFS)
#import sys
#input = sys.stdin.readline
from collections import deque

def bfs():
    visited = [[0]*m for _ in range(n)]
    q = deque()
    q.append([0,0])
    visited[0][0] = board[0][0]
    while q:
        x, y = q.popleft()
        for a,b in direction:
            nx = x + a
            ny = y + b
            if nx < n and ny < m :
                if visited[nx][ny] < visited[x][y]+board[nx][ny]:
                    visited[nx][ny] = visited[x][y]+board[nx][ny]
                    q.append([nx,ny])
                elif visited[x][y]+board[nx][ny] == 0 and visited[nx][ny] == 0 :
                    q.append([nx,ny])
    return visited[n-1][m-1]
    

n,m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
direction = [(1,0),(0,1)]
result = 0

print(bfs())
#BFS 방식도 90%에서 시간초과나 메모리 초과발생