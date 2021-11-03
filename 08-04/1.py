#https://www.acmicpc.net/problem/9095
#백준 1,2,3 더하기 (DP)
#import sys
#input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
target = max(nums)    
dp = [0] * (target+1)
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, target+1):
    dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
    
for num in nums:
    print(dp[num])