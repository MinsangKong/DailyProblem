#https://www.acmicpc.net/problem/11780
#백준 11780번 플로이드 2 (플로이드)
#import sys
#input = sys.stdin.readline

n = int(input())
m = int(input())

board = [[0]*n for _ in range(n)]
way = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a,b,c = map(int, input().split())
    if board[a-1][b-1]:
        board[a-1][b-1] = min(c,board[a-1][b-1])
    else:
        board[a-1][b-1] = c
    
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j :
                continue
            if board[i][k] and board[k][j]:
                if board[i][j] == 0 :
                    board[i][j] = board[i][k]+board[k][j]
                    way[i][j] = way[i][k]+[k+1]+way[k][j]
                elif board[i][j] > board[i][k]+board[k][j]:
                    board[i][j] = board[i][k]+board[k][j]
                    way[i][j] = way[i][k]+[k+1]+way[k][j]
                    
for i in board:
    print(*i)

for i in range(n):
    for j in range(n):
        if board[i][j] == 0 :
            print(0)
        else:
            print(len(way[i][j])+2,i+1,*way[i][j],j+1)