#https://www.acmicpc.net/problem/20162
#백준 20162번 간식 파티 (DP)
#import sys
#input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]

dp = [0]*n
dp[0] = nums[0]
for i in range(1,n):
    dp[i] = nums[i]
    for j in range(i-1,-1,-1):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i],dp[j]+nums[i])
print(max(dp))