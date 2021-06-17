#https://www.acmicpc.net/problem/13398
#백준 13398번 연속합2(DP)
#import sys
#input = sys.stdin.readline
from collections import deque

n = int(input())
nums = list(map(int, input().split()))

dp = [[-1001]*n for _ in range(3)]

dp[0][0] = nums[0] #결과가 양수이면 저장
dp[1][0] = nums[0] #양수만 저장
dp[2][0] = nums[0] #음수 1회 점프한 값 저장

for i in range(1,n):
    if nums[i] > 0:
        dp[0][i]= max(dp[0][i-1]+nums[i],nums[i])
        dp[1][i]= max(dp[1][i-1]+nums[i],nums[i])
        dp[2][i]= max(dp[2][i-1]+nums[i],nums[i])
    else:
        if dp[0][i-1]+nums[i] > 0:
            dp[0][i]= dp[0][i-1]+nums[i]
        else:
            dp[0][i]= nums[i]
        dp[1][i]= nums[i]
        dp[2][i] = max(dp[1][i-1],dp[0][i-1],nums[i],dp[2][i-1]+nums[i])
print(dp)
print(max(max(dp[0]),max(dp[1]),max(dp[2])))