#https://www.acmicpc.net/problem/18500
#백준 18500번 미네랄 2 (구현, 시뮬레이션)
#import sys
#input = sys.stdin.readline
from collections import deque

def isReachable(x,y,state):
    for a,b in movable[state]:
        nx = x+a
        ny = y+b
        cluster = set()
        if 0 <= nx < n and 0 <= ny < m :
            if board[nx][ny] == 'x':
                visited = [[0]*m for _ in range(n)]
                visited[nx][ny] = 1
                cluster = set()
                cluster.add((nx,ny))
                
                reachable = False
                q = deque([[nx,ny]])

                while q:
                    dx,dy = q.popleft()

                    for r2, c2  in direction:

                        moved_r = dx + r2
                        moved_c = dy + c2

                        if moved_c < 0 or moved_c > m-1 or moved_r < 0 or moved_r > n-1: continue

                        if board[moved_r][moved_c] == '.': continue
                        if visited[moved_r][moved_c]: continue
                        if moved_r == n-1: 
                            reachable = True 
                            break

                        q.append([moved_r, moved_c])
                        visited[moved_r][moved_c] = True
                        cluster.add((moved_r, moved_c))
        
                if not reachable:
                    moveCluster(cluster)
                    break            

def moveCluster(cluster):
    cnt = 0
    checked = [[0]*m for _ in range(n)]
    flag = True
    
    while flag:
        cnt += 1
        
        for x,y in cluster:
            if x+cnt == n-1:
                flag = False
                break
            if board[x+cnt+1][y] == 'x':
                if (x+cnt+1,y) not in cluster:
                    flag = False
                    break
                    
    for x,y in cluster:
        if not checked[x][y]:
            board[x][y] = '.'
        
        board[x+cnt][y] = 'x'
        checked[x+cnt][y] = 1

n,m = map(int,input().split())
board = [list(input().rstrip()) for _ in range(n)]

q = int(input())
queries = list(map(int, input().split()))
movable = [[[-1, 0], [0, 1], [1, 0]], [[-1, 0], [0, -1], [1, 0]]]
direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]

for i in range(q):
    pos = n-queries[i]
    y = -1
    if i%2 == 0 :
        for j in range(m):
            if board[pos][j] == 'x':
                y = j
                break
    else:
        for j in range(m-1,-1,-1):
            if board[pos][j] == 'x':
                y = j
                break

    if y != -1 :
        board[pos][j] = '.'
        isReachable(pos,y,i % 2)
        
for _map in board:
    print(''.join(_map))