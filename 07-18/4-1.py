#https://www.acmicpc.net/problem/1944
#백준 1944번 복제 로봇(구현, MST)
import sys
#input = sys.stdin.readline
from collections import deque

def bfs(sx,sy,ex,ey):
    q = deque()
    visited = [[0]*n for _ in range(n)]
    q.append((sx,sy))
    while q:
        x,y = q.popleft()
        if x == ex and y == ey:
            return visited[x][y]
        for a,b in direction:
            nx = a + x
            ny = b + y
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and board[nx][ny] != '1':
                    visited[nx][ny] = visited[x][y]+1
                    q.append((nx,ny))
    return -1

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
n, m = map(int, input().split())

board = [list(input().rstrip()) for _ in range(n)]
direction = [(1,0),(-1,0),(0,1),(0,-1)]
parent = [i for i in range(m+1)]

cases = [] 

for i in range(n):
    for j in range(n):
        if board[i][j] == 'S' or board[i][j] == 'K':
            cases.append((i,j)) 
            
edges = []

for i in range(m):
    for j in range(i+1,m+1):
        dist = bfs(cases[i][0],cases[i][1],cases[j][0],cases[j][1])
        if dist == -1:
            print(-1)
            sys.exit(0)
        edges.append([dist,i,j])
        
edges.sort()

result = 0
cnt = 0
for dist, a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        cnt += 1
        result += dist
        
    if cnt == m :
        break
    
print(result)
'''
sys.exit(0) => 프로그램을 정상적으로 종료시키고 싶을 때
sys.exit(1) => 프로그램을 비정상적으로라도, 강제적으로 종료시키고 싶을 때

'''