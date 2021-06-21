#https://www.acmicpc.net/problem/15653
#백준 15653번 구슬 탈출 4(BFS)
#import sys
#input = sys.stdin.readline
from collections import deque

def bfs(rx,ry,bx,by):
    q = deque()
    visited = [[[[0 for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
    visited[rx][ry][bx][by] = 1
    q.append([rx,ry,bx,by,1])
    direction = [[1,0],[-1,0],[0,1],[0,-1]]
    while q:
        rdx,rdy,bdx,bdy,cnt = q.popleft()
        for a,b in direction:
            rnx,rny,bnx,bny = rdx,rdy,bdx,bdy
            while True:
                rnx += a
                rny += b
                if board[rnx][rny] == 'O':
                    break
                elif board[rnx][rny] == '#':
                    rnx -= a
                    rny -= b
                    break
            
            while True:
                bnx += a
                bny += b
                if board[bnx][bny] == 'O':
                    break
                elif board[bnx][bny] == '#':
                    bnx -= a
                    bny -= b
                    break
                    
            if board[bnx][bny] == 'O':
                continue
            elif board[rnx][rny] == 'O':
                return cnt
            
            if rnx == bnx and rny == bny:
                if abs(rnx-rdx)+abs(rny-rdy) > abs(bnx-bdx)+abs(bny-bdy):
                    rnx -= a
                    rny -= b
                else:
                    bnx -= a
                    bny -= b
                    
            if visited[rnx][rny][bnx][bny] == 0:
                visited[rnx][rny][bnx][bny] = 1
                q.append([rnx,rny,bnx,bny,cnt+1])
                
    return -1

n, m = map(int, input().split())

board = []

for _ in range(n):
    board.append(list(input().rstrip()))
    
redX, redY = 0, 0
blueX, blueY = 0, 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            board[i][j] == '.'
            redX, redY = i, j
        elif board[i][j] == 'B':
            board[i][j] == '.'
            blueX, blueY = i, j
            
print(bfs(redX,redY,blueX,blueY))