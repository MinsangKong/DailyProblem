#https://www.acmicpc.net/problem/2839
#백준 2839번 설탕 배달(DP)
#import sys
#input = sys.stdin.readline

n = int(input())

if n <= 5 :
    if n == 3 or n == 5 :
        print(1)
    else:
        print(-1)
else:
    dp = [0]*(n+1)
    dp[3] = 1
    dp[5] = 1
    for i in range(6, n+1):
        if dp[i-3] > 0 and dp[i-5] > 0 :
            dp[i] = min(dp[i-3],dp[i-5])+1
        elif dp[i-3] > 0 :
            dp[i] = dp[i-3]+1
        elif dp[i-5] > 0 :
            dp[i] = dp[i-5]+1
            
    print(dp[n] if dp[n] > 0 else -1)