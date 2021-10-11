#https://www.acmicpc.net/problem/2407
#백준 2407번 조합(DP)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dp = [[0]*(m+1) for _ in range(n+1)]

dp[1][0] = 1
dp[1][1] = 1

for i in range(2,n+1):
    if i >= m:
        for j in range(m+1):
            if j == 0 :
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j]+dp[i-1][j-1]
    else:
        for j in range(i+1):
            if j == 0 or j == i:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j]+dp[i-1][j-1]

print(dp[n][m])