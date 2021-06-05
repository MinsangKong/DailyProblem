#https://www.acmicpc.net/problem/10026
#백준 10026번 적록색약(BFS)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(3000000)
def dfs(x,y,color):
    visited[x][y]=1
    for a,b in direction:
        dx = x+a
        dy = y+b
        if dx < 0 or dx >= n or dy < 0 or dy >= n:
            continue
        elif visited[dx][dy] == 0 and color == zone[dx][dy]:
            dfs(dx,dy,zone[dx][dy])

def dfs_weak(x,y,color):
    visited_weak[x][y]=1
    for a,b in direction:
        dx = x+a
        dy = y+b
        if dx < 0 or dx >= n or dy < 0 or dy >= n:
            continue
        elif visited_weak[dx][dy] == 0 and zone_weak[dx][dy]==color:
            dfs_weak(dx,dy,zone_weak[dx][dy])
    
n = int(input())
zone = []
zone_weak = []
visited = [[0]*n for _ in range(n)]
visited_weak = [[0]*n for _ in range(n)]
direction = [(1,0),(-1,0),(0,1),(0,-1)]
cnt = 0
cnt_weak = 0
for i in range(n):
    data = input()
    zone.append(data)
    data_weak = []
    for j in data:
        if j == "G":
            data_weak.append("R")
        else:
            data_weak.append(j)
    zone_weak.append(data_weak)

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 :
            dfs(i,j,zone[i][j])
            cnt+=1
        if visited_weak[i][j] == 0:
            dfs_weak(i,j,zone_weak[i][j])
            cnt_weak+=1

print(cnt, cnt_weak)