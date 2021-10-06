#https://www.acmicpc.net/problem/14728
#백준 14728번 벼락치기(누적합, 2차원 DP)
#import sys
#input = sys.stdin.readline

n, t = map(int, input().split())

dp = [[0]*(t+1) for _ in range(n+1)]
info = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n+1):
    for j in range(t+1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif info[i-1][0] <= j:
            dp[i][j] = max(dp[i-1][j], info[i-1][1] + dp[i-1][j-info[i-1][0]])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][t])