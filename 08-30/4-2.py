#https://www.acmicpc.net/problem/14442
#백준 14442번 벽 부수고 이동하기 2 (BFS)
#import sys
#input = sys.stdin.readline
from collections import deque

def bfs():
    visited = [[k+1]*m for _ in range(n)]
    visited[0][0] = 0
    q = deque([[0,0,0]])
    dist = 1
    while True :
        temp = deque()
        while q :
            cnt, x, y = q.popleft()
            #print(cnt,x,y)
            if (x,y) == (n-1,m-1):
                return dist

            for a,b in direction :
                nx = x+a
                ny = y+b
                if nx < 0 or nx >= n or ny < 0 or ny >= m :
                    continue
                if board[nx][ny] :
                    if cnt >= k :
                        continue
                    if visited[nx][ny] > cnt+1:
                        visited[nx][ny] = cnt+1
                        temp.append([cnt+1,nx,ny])
                else:
                    if visited[nx][ny] > cnt :
                        visited[nx][ny] = cnt
                        temp.append([cnt,nx,ny])
        if temp :
            q = temp
            dist += 1
        else:
            break
    return -1

n,m,k = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]
direction = [(0,1),(1,0),(0,-1),(-1,0)]

print(bfs())