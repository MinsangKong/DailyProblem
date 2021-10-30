#https://www.acmicpc.net/problem/17845
#백준 17845번 수강 과목 (DP)
#import sys
#input = sys.stdin.readline

n, k = map(int, input().split())

info = [list(map(int, input().split())) for _ in range(k)]

dp = [0]*(n+1)

for score, time in info:
    for i in range(n,time-1,-1):
        dp[i] = max(dp[i],dp[i-time]+score)
        
print(dp[n])