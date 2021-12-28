#https://www.acmicpc.net/problem/16954
#백준 16954번 움직이는 미로 탈출 (BFS)
#import sys
#input = sys.stdin.readline
from collections import deque

def bfs():
    q = deque([[7,0]])
    cnt = 0
    while True :
        temp = deque()
        visited = [[0]*8 for _ in range(8)]
        while q:
            x,y = q.popleft()
            if x == 0 and y == 7 :
                return 1
            if board[x][y] == '#':
                continue
            for a,b in direction :
                nx = x+a
                ny = y+b
                if 0 > nx or nx >= 8 or ny < 0 or ny >= 8 :
                    continue   
                if board[nx][ny] == '.' and not visited[nx][ny] :
                    temp.append([nx,ny])
                    visited[nx][ny] = 1 
                
        if not temp :
            break
        if cnt >= 8 :
            return 1
        q = temp
        cnt += 1
        changeBoard(cnt)
    return 0

def changeBoard(cnt):
    for i in range(7,cnt-1,-1):
        for j in range(8):
            board[i][j] = board[i-1][j]
    for j in range(8):
        board[cnt-1][j] = '.'

board = [list(input().rstrip()) for _ in range(8)]
direction = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1),(0,0)]
            
print(bfs())