#https://www.acmicpc.net/problem/16985
#백준 16985번 Maaaaaaaaaze (그래프이론, 구현)
#import sys
#input = sys.stdin.readline
from itertools import permutations
from collections import deque

def bfs(board):
    visited = [[[0]*5 for _ in range(5)] for _ in range(5)]
    if not board[0][0][0]:
        return -1
    
    visited[0][0][0] = 1
    q = deque([[0,0,0,0]])
    while q:
        z,x,y,cnt = q.popleft()
        if x == 4 and y == 4 and z == 4 :
            return cnt
        
        for c,a,b in direction:
            nz = z+c
            nx = x+a
            ny = y+b
            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5 or nz >= 5 or nz < 0 :
                continue
            if board[nz][nx][ny] and not visited[nz][nx][ny]:
                visited[nz][nx][ny] = 1
                q.append([nz,nx,ny,cnt+1])
    return -1

def rotate(plate):
    new = [[0]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            new[i][j] = plate[5-j-1][i]
    return new

boards = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
result = int(1e9)
direction = [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]

for value in permutations(boards,5):
    board = []
    for i in range(5):
        board.append(value[i])
    for _ in range(4):
        board[0] = rotate(board[0])
        for _ in range(4):
            board[1] = rotate(board[1])
            for _ in range(4):
                board[2] = rotate(board[2])
                for _ in range(4):
                    board[3] = rotate(board[3])
                    for _ in range(4):
                        board[4] = rotate(board[4])
                        num = bfs(board)
                        if num != -1 :
                            result = min(num,result)

print(result if result != int(1e9) else -1)  