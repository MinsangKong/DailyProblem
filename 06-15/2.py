#https://www.acmicpc.net/problem/17836
#백준 17836번 공주님을 구해라!(BFS)
#import sys
#input = sys.stdin.readline
import heapq

def bfs(t):
    q = []
    visited[0][0] = 0
    heapq.heappush(q,(0,0,0))
    while q:
        cnt,x,y = heapq.heappop(q)
        if cnt > t:
            break
        if x == n-1 and y == m-1:
            return 
        if visited[x][y] < cnt:
            continue
        
        for a, b in direction:
            dx = x+a
            dy = y+b
            if 0 <= dx < n and 0 <= dy < m:
                if visited[dx][dy] > cnt+1 and board[dx][dy] != 1:
                    visited[dx][dy] = cnt+1
                    if board[dx][dy] == 2:
                        visited[n-1][m-1] = min(cnt+1+abs(n-1-dx)+abs(m-1-dy),visited[n-1][m-1])
                    heapq.heappush(q,(cnt+1,dx,dy))
    return

n, m, t = map(int, input().split())

board = []

for _ in range(n):
    board.append(list(map(int, input().split())))
    
visited = [[int(1e9)]*m for _ in range(n)]
direction = [(1,0),(-1,0),(0,1),(0,-1)]

bfs(t)
if visited[n-1][m-1] <= t:
    print(visited[n-1][m-1])
else:
    print("Fail")