#https://www.acmicpc.net/problem/20058
#백준 20058번 마법사 상어와 파이어스톰(DFS, 구현)
#import sys
#input = sys.stdin.readline
from collections import deque

def rotate(n,l):
    sizeL = 2**l
    for i in range(0,n,sizeL):
        for j in range(0,n,sizeL):
            for k in range(2**(l-1)):
                left, right, up, down = j+k, i+k, j-k-1+sizeL, i-k-1+sizeL
                #print(left,right,up,down)
                endX = i-k-1+sizeL
                endY = j-k-1+sizeL
                while left < endY:
                    board[i+k][left], board[right][endY], board[endX][up], board[down][j+k] = board[down][j+k], board[i+k][left], board[right][endY], board[endX][up]
                    left += 1
                    right += 1
                    up -= 1
                    down -= 1

def bfs(x,y):
    q = deque()
    q.append([x,y])
    board[x][y] = 0
    total = 1
    while q:
        i,j = q.popleft()
        for a, b in direction :
            nx = i + a
            ny = j + b
            if 0 <= nx < 2**n and 0 <= ny < 2**n :
                if board[nx][ny] > 0:
                    board[nx][ny] = 0
                    total += 1
                    q.append([nx,ny])
    return total

def countIce():
    changed = []
    for i in range(2**n):
        for j in range(2**n):
            cnt = 0
            if board[i][j] == 0 :
                continue
            for a,b in direction:
                nx = i + a
                ny = j + b
                if 0 <= nx < 2**n and 0 <= ny < 2**n :
                    if board[nx][ny] > 0 :    
                        cnt+= 1
            if cnt < 3 :
                changed.append([i,j])
    for x,y in changed:
        board[x][y] -= 1

n, q = map(int, input().split())
sizeN = 2**n
board = [list(map(int, input().split())) for _ in range(sizeN)]
direction = [(1,0),(-1,0),(0,1),(0,-1)]

for k in list(map(int, input().split())):
    if k :
        rotate(sizeN,k)
    countIce() 
total = sum(map(sum, board))
islandMax = 0

for i in range(sizeN):
    for j in range(sizeN):
        if board[i][j] > 0:
            islandMax = max(islandMax, bfs(i,j))
print(total)
print(islandMax)
#어이가 없다... 입력과 동시에 list(map(int, input().split()))로 처리하는 방식만 메모리 초과가 발생안함
#후... 속도도 빠르게 작성했는데 좀 짜증이 난다...