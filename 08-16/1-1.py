#https://www.acmicpc.net/problem/1913
#백준 1913번 달팽이(Divide and Conquer)
#import sys
#input = sys.stdin.readline

n = int(input())
target = int(input())

board = [[0]*n for _ in range(n)]
cur = n**2
board[0][0] = cur
sx, sy = 0, 0
x,y = 0, 0


for _ in range(n//2+1):
    
    while True:
        cur -= 1
        sx += 1
        if sx >= n or board[sx][sy]:
            cur += 1
            sx -= 1
            break
        if cur == target:
            x,y = sx,sy
        board[sx][sy] = cur
    
    while True:
        cur -= 1
        sy += 1
        if sy >= n or board[sx][sy]:
            sy -= 1
            cur += 1
            break
        if cur == target:
            x,y = sx,sy
        board[sx][sy] = cur
        
    while True:
        cur -= 1
        sx -= 1
        if sx < 0 or board[sx][sy]:
            sx += 1
            cur += 1
            break
        if cur == target:
            x,y = sx,sy
        board[sx][sy] = cur
        
    while True:
        cur -= 1
        sy -= 1
        if sy < 0 or board[sx][sy]:
            sy += 1
            cur += 1
            break
        if cur == target:
            x,y = sx,sy
        board[sx][sy] = cur
        
for i in board:
    print(*i)
print(x+1,y+1)