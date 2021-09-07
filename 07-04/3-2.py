#https://www.acmicpc.net/problem/14500
#백준 14500번 테트로미노 (DFS, 백트래킹)
#import sys
#input = sys.stdin.readline

def dfs(x,y,depth,total):
    global result
    if depth == 4:
        result = max(result, total)
        return
    if result >= total+maxNum*(4-depth):
        return
    
    for a,b in direction:
        nx = x+a
        ny = y+b
        
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = 1
            if depth == 2:
                dfs(x,y,depth+1,total+board[nx][ny])
            dfs(nx,ny,depth+1,total+board[nx][ny])
            visited[nx][ny] = 0

n, m = map(int, input().split())
result = 0
direction = [(1,0),(-1,0),(0,1),(0,-1)]

board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
maxNum = max(map(max, board))

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i,j,1,board[i][j])
        visited[i][j] = 0
        
print(result)
#백트래킹 코드를 보고 작성하니까 불필요한 부분을 쳐냈기 때문에 확실히 빨랐다.