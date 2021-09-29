#https://www.acmicpc.net/problem/16724
#백준 16724번 피리 부는 사나이(구현, BFS)
#import sys
#input = sys.stdin.readline
from collections import deque

def bfs(x,y):
    q = deque()
    visited[x][y] = 1
    q.append((x,y))
    check = set()
    check.add((x,y))
    while q:
        dx, dy = q.popleft()
        way = board[dx][dy]
        
        nx = dx+direction[way][0]
        ny = dy+direction[way][1]
        
        if not visited[nx][ny]:
            visited[nx][ny] = 1
            q.append((nx,ny))
            check.add((nx,ny))
        elif (nx,ny) in check:
            return True
    return False

n, m = map(int, input().split())

board = [[0]*m for _ in range(n)]
direction = [(-1,0),(1,0),(0,-1),(0,1)]
book = {"U":0, "D":1, "L":2, "R":3}

for i in range(n):
    data = list(input().rstrip())
    for j in range(m):
        board[i][j]=book[data[j]]
        
visited = [[0]*m for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if bfs(i,j):
                cnt += 1
            
print(cnt)   