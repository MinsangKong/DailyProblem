#https://www.acmicpc.net/problem/11057
#백준 11057번 오르막 수 (DP)
#import sys
#input = sys.stdin.readline

n = int(input())

dp = [[0]*10 for _ in range(n)]

for i in range(10):
    dp[0][i] = 1
    
for i in range(1,n):
    for j in range(10):
        if j == 0 :
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = dp[i][j-1]+dp[i-1][j]
print(sum(dp[n-1])%10007)