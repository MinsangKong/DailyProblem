#https://www.acmicpc.net/problem/16234
#백준 16234번 인구 이동 (BFS)
import sys
#input = sys.stdin.readline
from collections import deque

def bfs(visited,pos,world):
    i, j = pos
    q = deque()
    q.append((i,j))
    nations = [(i,j)]
    visited[i][j] = 1
    while q:
        x,y = q.popleft()
        for a,b in direction:
            dx = x+a
            dy = y+b
            if 0 <= dx < n and 0 <= dy < n:
                if visited[dx][dy] == 0 and l <= abs(world[x][y]-world[dx][dy]) <= r:
                    visited[dx][dy] = 1
                    nations.append((dx,dy))
                    q.append((dx,dy))
                    
    if len(nations) == 1:
        return
    cost = 0
    for a,b in nations:
        cost+=world[a][b]
    avg = cost//len(nations)
    for a,b in nations:
        world[a][b] = avg
        
def check(world):
    visited = [[0]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                cnt+=1
                flag = False
                for a,b in direction:
                    dx = a+i
                    dy = b+j
                    if 0 <= dx < n and 0 <= dy < n:
                        if visited[dx][dy] == 0 and l <= abs(world[i][j]-world[dx][dy]) <= r:
                            flag = True
                            break
                if flag:
                    bfs(visited,(i,j),world)
                else:
                    visited[i][j] = 1
    return cnt

n, l, r = map(int, input().split()) 
world = [list(map(int, input().split())) for _ in range(n)]
direction = [(1,0),(-1,0),(0,1),(0,-1)]
result = 0

result = 0
while True:
    k = check(world)
    if k == n*n:
        print(result)
        sys.exit(0)
    result +=1