#https://www.acmicpc.net/problem/20181
#백준 20181번 꿈틀꿈틀 호석 애벌레 - 효율성(DP, 누적합)
#import sys
#input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))

dp = [0] * n

subSum = nums[0]
subIdx = 0

if nums[0] >= k:
    dp[0] = nums[0]-k
    subSum = 0
    subIdx = 1

for i in range(1,n):
    subSum += nums[i]
    dp[i] = dp[i-1]
    while subSum >= k:
        dp[i] = max(dp[i], dp[subIdx-1]+subSum-k)
        subSum -= nums[subIdx]
        subIdx += 1
#print(dp)
print(dp[-1])
#역시 시간 복잡도 문제를 해결하기 위해서는 누적합 + DP를 활용한 방식으로 풀어야 했다.