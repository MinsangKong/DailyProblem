#https://www.acmicpc.net/problem/12865
#백준 12865번 평범한 배낭(DP)
#import sys
#input = sys.stdin.readline

n, k = map(int, input().split())
bags = []
dp = [[0]*(k+1) for _ in range(n+1)]
result = 0
for _ in range(n):
    bags.append(list(map(int, input().split())))
    
for i in range(1,n+1):
    for j in range(1,k+1):
        if j >= bags[i-1][0]:
            dp[i][j] = max(dp[i-1][j], (dp[i-1][j-bags[i-1][0]])+bags[i-1][1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][k])