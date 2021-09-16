#https://www.acmicpc.net/problem/14503
#백준 14503번 로봇 청소기(DFS)
#import sys
#input = sys.stdin.readline

def dfs(x,y,d):
    global result
    if not board[x][y]:
        board[x][y] = 2
        result+=1
    turn = d
        
    for i in range(4):
        if turn == 0:
            turn += 3
        else:
            turn -= 1
        nx = x+direction[turn][0]
        ny = y+direction[turn][1]
        if not board[nx][ny]:
            dfs(nx,ny,turn)
            return 

    nx = x-direction[d][0]
    ny = y-direction[d][1]
    if board[nx][ny] != 1:
        dfs(nx,ny,d)

n, m = map(int, input().split())

x, y, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
direction = [(-1,0),(0,1),(1,0),(0,-1)]

result = 0

dfs(x,y,d)

print(result)