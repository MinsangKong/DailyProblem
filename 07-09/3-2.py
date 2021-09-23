#https://www.acmicpc.net/problem/20058
#백준 20058번 마법사 상어와 파이어스톰(DFS, 구현)
import sys
#input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def rotate(n,l):
    sizeN = 2**n
    sizeL = 2**l
    for i in range(0,sizeN,sizeL):
        for j in range(0,sizeN,sizeL):
            temp = [board[x][j:j+sizeL] for x in range(i, i+sizeL)]
            for x in range(sizeL):
                for y in range(sizeL):
                    board[i+y][j+sizeL-1-x] = temp[x][y]
    
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
#복사 후 붙여넣기 하는 방식으로도 메모리 초과 및 시간 초과 발생...