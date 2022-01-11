#https://www.acmicpc.net/problem/2435
#백준 2435번 기상청 인턴 신현수 (누적합)
#import sys
#input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))
dp = [0]*(n+1)
result = -101

for i in range(n):
    dp[i+1] = dp[i]+nums[i]
    
for i in range(n-k+1):
    result = max(dp[i+k]-dp[i], result)
print(result)