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
    cnt = 0
    while True:
        temp = deque()
        while q :
            rx,ry,bx,by = q.popleft()
            #print(rx,ry,bx,by)
            for a,b in direction:
                flag = True
                nrx = rx
                nry = ry
                nbx = bx
                nby = by
                rc = 0
                while True:
                    if board[nrx][nry] == 'O':
                        break
                    if board[nrx][nry] == '#':
                        nrx -= a
                        nry -= b
                        rc -= 1
                        break
                    nrx += a
                    nry += b
                    rc += 1
                while True:
                    if board[nbx][nby] == 'O':
                        flag = False
                        break
                    if board[nbx][nby] == '#':
                        nbx -= a
                        nby -= b
                        rc += 1
                        break
                    nbx += a
                    nby += b
                    rc -= 1
                if not flag:
                    continue
                if board[nrx][nry] == 'O':
                    return 1
                if nrx == nbx and nry == nby:
                    if rc >= 0:
                        nrx -= a
                        nry -= b
                    else:
                        nbx -= a
                        nby -= b
                if not visited[nrx][nry][nbx][nby] :
                    visited[nrx][nry][nbx][nby] = 1
                    temp.append([nrx,nry,nbx,nby])
                        
        if not temp :
            return 0
        cnt += 1
        if cnt == 10 :
            return 0
        q = temp

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
#바보처럼 10번 세기를 잘못해서 계속 틀렸다