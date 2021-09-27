#https://www.acmicpc.net/problem/17472
#백준 17472번 다리 만들기 2 (BFS, 크루스컬, 구현)
#import sys
#input = sys.stdin.readline
from collections import deque

def bfs(x, y, idx):
    q = deque()
    board[x][y] = idx
    q.append((x,y))
    while q:
        dx, dy = q.popleft()
        
        for a,b in direction:
            nx = dx+a
            ny = dy+b
            if 0 <= nx < n and 0 <= ny < m :
                if board[nx][ny] == 1 :
                    board[nx][ny] = idx
                    q.append((nx,ny))
                    
def find_island(islands, x):
    if islands[x] != x:
        islands[x] = find_island(islands, islands[x])
    return islands[x]

def union_island(islands, a, b):
    a = find_island(islands, a)
    b = find_island(islands, b)
    if a < b:
        islands[b] = a
    else:
        islands[a] = b
        
def find_edge(x, y, idx):
    for a, b in direction:
        nx = x+a
        ny = y+b
        cnt = 0
        while True:
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == idx:
                    break
                elif not board[nx][ny]:
                    nx += a
                    ny += b
                    cnt += 1
                else:
                    if cnt < 2 :
                        break
                    target = board[nx][ny]
                    if not distance[idx-2][target-2]:
                        distance[idx-2][target-2] = cnt
                    else:
                        distance[idx-2][target-2] = min(cnt, distance[idx-2][target-2])
                    break
            else:
                break

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
direction = [(1,0),(-1,0),(0,1),(0,-1)]
idx = 2
islands = [i for i in range(6)]
distance = [[0]*6 for _ in range(6)]
costs = set()

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            bfs(i,j,idx)
            idx+=1
            
for i in range(n):
    for j in range(m):
        if board[i][j]:
            find_edge(i,j,board[i][j])
            
for i in range(6):
    for j in range(6):
        if distance[i][j]:
            costs.add((distance[i][j], i, j))

result = 0

for cost, a, b in sorted(costs, key = lambda x : x[0]):
    if find_island(islands, a) != find_island(islands, b):
        result += cost
        union_island(islands, a, b)
        
for i in range(idx-2):
    if find_island(islands, i) != 0 :
        result = -1
        break
        
print(result)
#마지막에 순환 여부를 체크할 때 크루스컬 내부에서 처리하는 것보다 빼서 별개로 돌리는게 빨랐다.