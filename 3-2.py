#https://www.acmicpc.net/problem/14925
#백준 14925번 목장 건설하기 (DP)
#import sys
#input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        if board[i-1][j-1]:
            dp[i][j] = 0
        else:
            dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
            
print(max(map(max, dp)))
#항상 이런 계통 문제는 완탐 시도 후 DP를 적용하게 된다...