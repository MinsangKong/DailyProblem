#https://www.acmicpc.net/problem/11048
#백준 11048번 이동하기 (DFS, 백트래킹)
import sys
#input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x,y,total):
    global result
    if x == n-1 and y == m-1 :
        result = max(result,total)
        return
    for a,b in direction:
        nx = x + a
        ny = y + b
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny]:
                visited[nx][ny] = 1
                dfs(nx,ny,total+board[nx][ny])
                visited[nx][ny] = 0

n,m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
direction = [(1,0),(0,1)]
result = 0

visited = [[0]*m for _ in range(n)]
visited[0][0] = 1

dfs(0,0,board[0][0])

print(result)
#DFS 백트래킹 방식은 시간초과 발생