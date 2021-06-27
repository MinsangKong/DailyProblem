#https://www.acmicpc.net/problem/14852
#백준 14852번 타일 채우기3(DP)
#import sys
#input = sys.stdin.readline

n = int(input())

if n == 1:
    print(2)
elif n == 2:
    print(7)
else:
    dp = [[0]*2 for _ in range(n+1)]
    dp[0][0] = 1
    dp[1][0] = 2
    dp[0][1] = 0
    dp[1][1] = 1
    for i in range(2, n+1):
        dp[i][1] = (dp[i-2][0]+dp[i-1][0]+dp[i-2][1]) %1000000007
        dp[i][0] = (dp[i-2][0]+2*dp[i][1]) %1000000007
    print(dp[n][0]%1000000007)