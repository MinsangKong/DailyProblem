#https://www.acmicpc.net/problem/13459
#백준 13459번 구슬 탈출 (BFS)
#import sys
#input = sys.stdin.readline
from collections import deque

def bfs(red,blue):
    q = deque([[red[0],red[1],blue[0],blue[1]]])
    direction = [(0,1),(0,-1),(1,0),(-1,0)]
    visited = [[[[0]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    visited[red[0]][red[1]][blue[0]][blue[1]] = 1
    cnt = 1
    while q :
        length = len(q)
        for _ in range(length):
            rx,ry,bx,by = q.popleft()
            for a,b in direction:
                nrx = rx
                nry = ry
                nbx = bx
                nby = by
                while True:
                    nrx += a
                    nry += b
                    if board[nrx][nry] == 'O':
                        break
                    if board[nrx][nry] == '#':
                        nrx -= a
                        nry -= b
                        break
                while True:
                    nbx += a
                    nby += b
                    if board[nbx][nby] == 'O':
                        break
                    if board[nbx][nby] == '#':
                        nbx -= a
                        nby -= b
                        break
                if board[nbx][nby] == 'O':
                    continue
                if board[nrx][nry] == 'O':
                    return 1
                if nrx == nbx and nry == nby:
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):
                        nrx -= a
                        nry -= b
                    else:
                        nbx -= a
                        nby -= b
                if not visited[nrx][nry][nbx][nby] :
                    visited[nrx][nry][nbx][nby] = 1
                    q.append([nrx,nry,nbx,nby])
        cnt += 1
        if cnt > 10 :
            return 0
    return 0

n, m = map(int, input().split())
board = []
red = [0,0]
blue = [0,0]

for i in range(n):
    data = list(input().rstrip())
    for j in range(m):
        if data[j] == 'B':
            blue = [i,j]
            data[j] = '.'
        elif data[j] == 'R':
            red = [i,j]
            data[j] = '.'
    board.append(data)

print(bfs(red,blue))