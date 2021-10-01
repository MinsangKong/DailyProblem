#https://www.acmicpc.net/problem/11055
#백준 11055번 가장 큰 증가 부분 수열(DP, LIS)
#import sys
#input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

dp = [0]*n
dp[0] = nums[0]
result = nums[0]

for i in range(1,n):
    temp = 0
    for j in range(i-1,-1,-1):
        if nums[i] > nums[j]:
            temp = max(temp,dp[j])
        
    dp[i] = temp+nums[i]
    result = max(result,dp[i])
        
#print(dp)
print(result)