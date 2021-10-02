#https://www.acmicpc.net/problem/10164
#백준 10164번 격자상의 경로(DP)
#import sys
#input = sys.stdin.readline

n, m, k = map(int, input().split())

board = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        board[i][j] = i*m + j+1
        
dp = [[0]*m for _ in range(n)]
dp[0][0] = 1

if k == 0 :
    for i in range(n):
        for j in range(m):
            if i > 0 and j > 0:
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
            elif i > 0 :
                dp[i][j] = dp[i-1][j]
            elif j > 0 :
                dp[i][j] = dp[i][j-1]
    print(dp[n-1][m-1])
else:
    x, y = divmod(k-1, m)
    #print(x, y)
    for i in range(x+1):
        for j in range(y+1):
            if i > 0 and j > 0:
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
            elif i > 0 :
                dp[i][j] = dp[i-1][j]
            elif j > 0 :
                dp[i][j] = dp[i][j-1]
    for i in range(x,n):
        for j in range(y,m):
            if i > x and j > y:
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
            elif i > x :
                dp[i][j] = dp[i-1][j]
            elif j > y :
                dp[i][j] = dp[i][j-1]
    print(dp[n-1][m-1])