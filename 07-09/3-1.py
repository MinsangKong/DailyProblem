#https://www.acmicpc.net/problem/20058
#백준 20058번 마법사 상어와 파이어스톰(DFS, 구현)
import sys
#input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def rotate(n,l):
    for i in range(0,2**n,2**l):
        for j in range(0,2**n,2**l):
            for k in range(2**(l-1)):
                left, right, up, down = j+k, i+k, j-k-1+2**l, i-k-1+2**l
                #print(left,right,up,down)
                endX = i-k-1+2**l
                endY = j-k-1+2**l
                while left < endY:
                    board[i+k][left], board[right][endY], board[endX][up], board[down][j+k] = board[down][j+k], board[i+k][left], board[right][endY], board[endX][up]
                    left += 1
                    right += 1
                    up -= 1
                    down -= 1

def dfs(x,y):
    board[x][y] = 0
    total = 1
    for a, b in direction :
        nx = x + a
        ny = y + b
        if 0 <= nx < 2**n and 0 <= ny < 2**n :
            if board[nx][ny] :
                total += dfs(nx,ny)
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

board = [list(map(int, input().split())) for _ in range(2**n)]
direction = [(1,0),(-1,0),(0,1),(0,-1)]

l = list(map(int, input().split()))

for k in range(q):
    if l[k] :
        rotate(n,l[k])
    countIce() 
total = sum(map(sum, board))
islandMax = 0

for i in range(2**n):
    for j in range(2**n):
        if board[i][j] > 0:
            target = dfs(i,j)
            islandMax = max(islandMax, target)
    
print(total)
print(islandMax)
#어떻게 처리하든 시간초과 발생
#rotation하는 과정에서 메모리 초과가 발생하는 것 같다