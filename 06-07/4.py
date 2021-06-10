#https://www.acmicpc.net/problem/15644
#백준 15644번 구슬 탈출3(BFS)
#import sys
#input = sys.stdin.readline
from collections import deque

def bfs(rx, ry, bx, by):
    cnt = 1
    q = deque()
    q.append([rx,ry,bx,by,""])
    visited[rx][ry][bx][by] = 1
    while q:
        qlen = len(q)
        for _ in range(qlen):
            drx, dry, dbx, dby, d = q.popleft()
            for i in range(4):
                nrx, nry, nbx, nby = drx, dry, dbx, dby
                while True:
                    nrx += direction[i][0]
                    nry += direction[i][1]
                    if boards[nrx][nry] == 'O':
                        break
                    if boards[nrx][nry] == '#':
                        nrx -= direction[i][0]
                        nry -= direction[i][1]
                        break

                while True:
                    nbx += direction[i][0]
                    nby += direction[i][1]
                    if boards[nbx][nby] == 'O':
                        break
                    if boards[nbx][nby] == '#':
                        nbx -= direction[i][0]
                        nby -= direction[i][1]
                        break
                        
                if boards[nbx][nby] == 'O':
                    continue
                if boards[nrx][nry] == 'O':
                    print(cnt)
                    print(d+op[i])
                    return
                    
                if nrx == nbx and nry == nby:
                    if abs(nrx - drx) + abs(nry - dry) > abs(nbx - dbx) + abs(nby - dby):
                        nrx -= direction[i][0]
                        nry -= direction[i][1]
                    else:
                        nbx -= direction[i][0]
                        nby -= direction[i][1]
                            
                if visited[nrx][nry][nbx][nby] == 0:
                    visited[nrx][nry][nbx][nby] = 1
                    q.append([nrx, nry, nbx, nby, d + op[i]])
                        
        cnt+=1
        if cnt > 10:
            print(-1)
            return
        
    print(-1)
    return
                        
n, m = map(int, input().split())
direction=[(0,1),(0,-1),(1,0),(-1,0)]
op = ['R','L','D','U']
boards = []

for _ in range(n):
    boards.append(list(input().rstrip()))
    
redX,redY = 0,0
blueX,blueY = 0,0

for i in range(n):
    for j in range(m):
        if boards[i][j] == 'R':
            redX,redY = i,j
            boards[i][j] = '.'
        elif boards[i][j] == 'B':
            blueX,blueY = i,j
            boards[i][j] = '.'
            
visited = [[[[0 for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
bfs(redX,redY,blueX,blueY)