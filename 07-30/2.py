#https://www.acmicpc.net/problem/4095
#백준 4095번 최대 정사각형 (DP)
#import sys
#input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0 :
        break
    board = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if board[i-1][j-1]:
                if dp[i][j-1] and dp[i-1][j] and dp[i-1][j-1]:
                    dp[i][j] = min(dp[i][j-1],dp[i-1][j-1],dp[i-1][j])+1
                else:
                    dp[i][j] = 1
    #print(*dp)
    print(max(map(max,dp)))