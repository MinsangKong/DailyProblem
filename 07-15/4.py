#https://www.acmicpc.net/problem/17090
#백준 17090번 미로 탈출하기 (BFS, 구현)
#import sys
#input = sys.stdin.readline
from collections import deque

def bfs(x,y):
    q = deque()
    cnt = 1
    visited[x][y] = 1
    q.append((x,y))
    check = [(x,y)]
    flag = True
    while q:
        dx, dy = q.popleft()
        way = board[dx][dy]
        nx = dx +direction[way][0]
        ny = dy +direction[way][1]
        
        if 0 <= nx < n and 0 <= ny < m :
            if not visited[nx][ny]:
                cnt += 1
                visited[nx][ny] = 1
                q.append((nx,ny))
                check.append((nx,ny))
            elif visited[nx][ny] == 2:
                break
            elif abs(visited[nx][ny]) == 1 :
                flag = False
                break
    if flag : 
        for a,b in check:
            visited[a][b] = 2
        return cnt
    else:
        for a,b in check:
            visited[a][b] = -1
        return 0

n, m = map(int, input().split())
board = [[0]*m for _ in range(n)]
visited = [[0]*m for _ in range(n)]

direction = [(1,0),(-1,0),(0,-1),(0,1)]
book = {'D':0, 'U':1, 'L':2, 'R':3}
result = 0

for i in range(n):
    data = input().rstrip()
    for j in range(m):
        board[i][j] = book[data[j]]
        
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            result += bfs(i,j)
            
#print(visited)
print(result)