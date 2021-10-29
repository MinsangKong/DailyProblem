#https://www.acmicpc.net/problem/20002
#백준 20002번 사과나무 (DP)
#import sys
#input = sys.stdin.readline

def check(limit):
    cnt = -1001
    for i in range(1,n+1-limit):
        for j in range(1,n+1-limit):
            cnt = max(cnt,dp[i+limit][j+limit]-dp[i+limit][j-1]-dp[i-1][j+limit]+dp[i-1][j-1])
    return cnt

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(n+1) for _ in range(n+1)]
result = -1001

for i in range(1,n+1):
    for j in range(1,n+1):
        dp[i][j] = dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]+board[i-1][j-1]
        
for i in range(n):
    result = max(check(i),result)
    
print(result)