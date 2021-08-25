#https://www.acmicpc.net/problem/10870
#백준 10870 피보나치수열 5(수학, DP)
#import sys
#input = sys.stdin.readline

n = int(input())

dp = [0]*21
dp[1] = 1

for i in range(2,21):
    dp[i] = dp[i-1]+dp[i-2]
    
print(dp[n])