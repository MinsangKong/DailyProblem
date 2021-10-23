#https://www.acmicpc.net/problem/12026
#백준 12026번 BOJ거리 (BFS)
#import sys
#input = sys.stdin.readline
INF = int(1e9)

n = int(input())
board = list(input().rstrip())
for i in range(n):
    if board[i] == 'B':
        board[i] = 0
    elif board[i] == 'O':
        board[i] = 1
    else:
        board[i] = 2
        
dp = [INF]*n
dp[0] = 0

for i in range(n-1):
    target = (board[i]+1)%3
    for j in range(i+1,n):
        if board[j] == target:
            dp[j] = min(dp[j],(j-i)**2+dp[i])
            
if dp[n-1] < INF :
    print(dp[n-1])
else:
    print(-1)