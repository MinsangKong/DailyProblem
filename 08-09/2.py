#https://www.acmicpc.net/problem/11123
#백준 11123번 양 한마리... 양 두마리...
#import sys
#input = sys.stdin.readline

def dfs(x, y):
    visited[x][y] = 1
    q = []
    q.append([x,y])
    while q:
        dx, dy = q.pop()
        for a, b in direction:
            nx, ny = dx+a, dy+b
            if 0 <= nx < h and 0 <= ny < w:
                if not visited[nx][ny] and board[nx][ny] == '#':
                    visited[nx][ny] = 1
                    q.append([nx,ny])

t = int(input())
direction = [(-1,0), (1,0), (0,-1), (0,1)]
for _ in range(t):
    ans = 0
    h, w = map(int, input().split())
    board = [list(input().strip()) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and board[i][j] == '#':
                dfs(i, j)
                ans += 1
    print(ans)