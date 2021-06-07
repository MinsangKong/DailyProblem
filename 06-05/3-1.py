#https://www.acmicpc.net/problem/6087
#백준 6087번 레이저 통신(BFS)
#import sys
#input = sys.stdin.readline
from collections import deque

def bfs(x,y,ex,ey):
    q = deque()
    direction = [(1,0),(0,1),(-1,0),(0,-1)]
    for i in range(4):
        nx = x+direction[i][0]
        ny = y+direction[i][1]
        if 0 <= nx < h and 0 <= ny < w and maps[nx][ny] != '*':
            visited[nx][ny][i] = 0
            q.append((nx,ny,i))
    while q:
        dx, dy, direct = q.popleft()

        for i in range(4):
            nx = dx+direction[i][0]
            ny = dy+direction[i][1]
            if 0 <= nx < h and 0 <= ny < w:
                
                cnt = visited[dx][dy][direct]
                if direct == 0 or direct == 2:
                    if i == 1 or i == 3:
                        cnt += 1
                else:
                    if i == 0 or i == 2:
                        cnt += 1
                if visited[nx][ny][i] == -1:  
                    visited[nx][ny][i] = cnt
                    q.append((nx, ny, i))
                else:  
                    if visited[nx][ny][i] > cnt:
                        visited[nx][ny][i] = cnt
                        q.append((nx, ny, i))        
    return min(visited[ex][ey])
w, h = map(int, input().split())
maps = []
laser = []
for i in range(h):
    data = list(input())
    maps.append(data)
    for j in range(w):
        if data[j] == 'C':
            laser.append([i,j])

    
visited = [[[int(1e9)] * 4 for _ in range(w)] for _ in range(h)]

print(bfs(laser[0][0],laser[0][1],laser[1][0],laser[1][1]))