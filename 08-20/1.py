#https://www.acmicpc.net/problem/13699
#백준 13699번 점화식 (DP)
#import sys
#input = sys.stdin.readline

n = int(input())
dp = [0]*(n+1)

dp[0] = 1

for i in range(1,n+1):
    for j in range(i):
        dp[i] += dp[j]*dp[i-j-1]

print(dp[n])