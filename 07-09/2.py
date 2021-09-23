#https://www.acmicpc.net/problem/5212
#백준 5212번 지구 온난화(BFS, 구현)
#import sys
#input = sys.stdin.readline
from collections import deque

def bfs():
    changed = []
    while islands :
        x, y = islands.popleft()
        cnt = 0
        for a,b in direction:
            nx = x+a
            ny = y+b
            if 0 <= nx < r and 0 <= ny < c:
                if board[nx][ny] == '.':
                    cnt+=1
            else:
                cnt+=1
        if cnt >= 3:
            changed.append((x,y))
            
    for x,y in changed :
        board[x][y] = '.'
        
def changed(idx):
    for i in range(r):
        if board[i][idx] == 'X':
            return False
    return True
            
r, c = map(int, input().split())
direction = [(1,0),(-1,0),(0,1),(0,-1)]
islands = deque()

board = [list(input()) for _ in range(r)]

for i in range(r):
    for j in range(c):
        if board[i][j] == 'X':
            islands.append((i,j))
            
bfs()

changedBoard = []

startX, endX, startY, endY= 0, 0, 0, c-1
for i in range(r):
    if 'X' in board[i]:
        startX = i
        break
for i in range(r-1,-1,-1):
    if 'X' in board[i]:
        endX = i
        break
        
while True:
    if changed(startY):
        startY += 1
    else:
        break
while True:
    if changed(endY):
        endY -= 1
    else:
        break

for i in range(startX, endX+1):
    for j in range(startY, endY+1):
        print(board[i][j], end='')
    print()