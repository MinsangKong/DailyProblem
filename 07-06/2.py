#https://www.acmicpc.net/problem/11053
#백준 11053번 가장 긴 증가하는 부분 수열(LIS)
#import sys
#input = sys.stdin.readline
import bisect

n = int(input())
nums = list(map(int, input().split()))

dp = [nums[0]]
for i in range(1, n):
    if dp[-1] < nums[i]:
        dp.append(nums[i])
    else:
        dp[bisect.bisect_left(dp,nums[i])] = nums[i]
        
print(len(dp))