#https://www.acmicpc.net/problem/10711
#백준 10711번 모래성(BFS)
#import sys
#input = sys.stdin.readline
from collections import deque

direction = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

h, w = map(int, input().split())

board = [list(input().rstrip()) for _ in range(h)]
visited = [[0]*w for _ in range(h)]
checkList = deque()

for i in range(h):
    for j in range(w):
        if board[i][j] == '.':
            board[i][j] = 0
            checkList.append([i,j])
        else:
            board[i][j] = int(board[i][j])
                
result = 0

while checkList:
    x, y = checkList.popleft()
    for a,b in direction:
        nx = x+a
        ny = y+b
        if 0 <= nx < h and 0 <= ny < w:
            if board[nx][ny] != 0:
                board[nx][ny] -= 1
                if board[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y]+1
                    result = max(result, visited[nx][ny])
                    checkList.append([nx,ny])
print(result)