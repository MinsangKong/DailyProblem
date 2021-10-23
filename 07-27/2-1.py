#https://www.acmicpc.net/problem/12026
#백준 12026번 BOJ거리 (BFS)
#import sys
#input = sys.stdin.readline
from collections import deque
INF = int(1e9)

def bfs():
    visited = [INF]*n
    visited[0] = 0
    q = deque()
    q.append(0)
    while q :
        now = q.popleft()
        target = (board[now]+1)%3
        for i in range(now+1,n):
            if board[i] == target and visited[i] > (i-now)**2+visited[now]:
                visited[i] = (i-now)**2+visited[now]
                q.append(i)
    if visited[n-1] < INF :
        return visited[n-1]
    else:
        return -1     

n = int(input())
board = list(input().rstrip())
for i in range(n):
    if board[i] == 'B':
        board[i] = 0
    elif board[i] == 'O':
        board[i] = 1
    else:
        board[i] = 2

print(bfs())