#https://www.acmicpc.net/problem/2748
#백준 2748번 피보나치 수 2(DP)
#import sys
#input = sys.stdin.readline

n = int(input())
dp = [0]*(n+1)
dp[1] = 1

for i in range(2,n+1):
    dp[i] = dp[i-1]+dp[i-2]
    
print(dp[n])