#https://www.acmicpc.net/problem/18808
#백준 18808번 스티커 붙이기 (구현, 백트래킹)
#import sys
#input = sys.stdin.readline

def check(sticker):
    start = sticker[0][0]
    sx, sy = len(sticker), len(sticker[0])
    for i in range(n-sx+1):
        for j in range(m-sy+1):
            if not board[i][j] or not start:
                if isPossible(i,j,sticker):
                    putBoard(i,j,sticker)
                    return True
    return False
                    
def isPossible(x,y,sticker):
    sx, sy = len(sticker), len(sticker[0])
    for i in range(x, sx+x):
        for j in range(y, sy+y):
            if sticker[i-x][j-y] and board[i][j]:
                return False
    return True

def putBoard(x,y,sticker):
    sx, sy = len(sticker), len(sticker[0])
    for i in range(x, sx+x):
        for j in range(y, sy+y):
            if sticker[i-x][j-y]:
                board[i][j] = 1

def rotate(sticker):
    y, x = len(sticker[0]), len(sticker)
    stickerNew = []
    for i in range(y):
        data = [0]*x
        for j in range(x-1,-1,-1):
            data[x-1-j] = sticker[j][i]
        stickerNew.append(data)
    return stickerNew
                
n, m, k = map(int, input().split())
board = [[0]*m for _ in range(n)]

for k in range(k):
    x, y = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(x)]
    for _ in range(4):
        if check(data):
            break
        data = rotate(data)
        
#for i in board:
#    print(*i)
print(sum(map(sum, board)))