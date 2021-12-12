#https://www.acmicpc.net/problem/13707
#백준 13707번 합분해 2 (DP)
#import sys
#input = sys.stdin.readline
INF = int(1e9)

n, k = map(int, input().split())
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,k+1):
        if i == 1 :
            dp[i][j] = j
        else:
            dp[i][j] = (dp[i-1][j]+dp[i][j-1])%INF
            
print(dp[n][k]%INF)