#https://www.acmicpc.net/problem/16926
#백준 16926번 배열 돌리기 1 (구현)
#import sys
#input = sys.stdin.readline

def rotate():
    newBoard = [[0]*m for _ in range(n)]
    for i in range(limit):
        change(i,newBoard)
    return newBoard

def change(cnt,newBoard):
    x,y = cnt, cnt
    while True :
        if x+1 >= n-cnt :
            break
        newBoard[x+1][y] = board[x][y]
        x += 1
    while True :
        if y+1 >= m-cnt :
            break
        newBoard[x][y+1] = board[x][y]
        y += 1
    while True :
        if x-1 < cnt :
            break
        newBoard[x-1][y] = board[x][y]
        x -= 1
    while True :
        if y-1 < cnt :
            break
        newBoard[x][y-1] = board[x][y]
        y -= 1

n,m,r = map(int, input().split())
limit = min(n,m)//2

board = [list(map(int, input().split())) for _ in range(n)]
for i in range(r):
    board = rotate()
    
for line in board:
    print(*line)