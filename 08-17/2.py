#https://www.acmicpc.net/problem/11660
#백준 11660번 구간 합 구하기 5 (누적합)
#import sys
#input = sys.stdin.readline

n, m = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(n+1) for _ in range(n+1)]

for i in range(n):
    for j in range(n):
        dp[i+1][j+1] = dp[i][j+1]+dp[i+1][j]-dp[i][j]+nums[i][j]

for _ in range(m):
    x1,y1,x2,y2 = map(int, input().split())
    result = dp[x2][y2]
    base = dp[x1-1][y2]+dp[x2][y1-1]-dp[x1-1][y1-1]
    print(result-base)