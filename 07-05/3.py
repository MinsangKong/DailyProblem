#https://www.acmicpc.net/problem/14502
#백준 14502번 연구소(BFS, 백트래킹)
#import sys
#input = sys.stdin.readline
from collections import deque
import copy

def bfs():
    global max_zero
    new_board = copy.deepcopy(board)
    q = deque()
    num = 0
    for a,b in virus:
        q.append((a,b))
    while q:
        x, y = q.popleft()
        for a,b in direction:
            dx = x+a
            dy = y+b
            if dx < 0 or dx >= n or dy < 0 or dy >=m:
                continue
            elif new_board[dx][dy] == 0:
                new_board[dx][dy] = 2
                q.append((dx,dy))
    
    for i in new_board:
        for j in i:
            if j == 0:
                num+=1
    max_zero = max(max_zero, num)
    
def wall(cnt):
    if cnt == 3:
        bfs()
        return
    else:
        for i in range(n):
            for j in range(m):
                if board[i][j] == 0:
                    board[i][j] = 1
                    wall(cnt+1)
                    board[i][j] = 0
    

n, m = map(int, input().split())
board = []
virus = []
max_zero = 0

for _ in range(n):
    board.append(list(map(int, input().split())))
    
direction = [(1,0), (-1,0), (0,1), (0,-1)]

for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            virus.append((i,j))
            
wall(0)
print(max_zero)