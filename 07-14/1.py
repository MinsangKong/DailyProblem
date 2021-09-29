#https://www.acmicpc.net/problem/15489
#백준 15489번 파스칼 삼각형(DP)
#import sys
#input = sys.stdin.readline

r, c, w = map(int, input().split())

limit = r+w-1

dp = [[0]*limit for _ in range(limit)]

for i in range(limit):
    for j in range(i+1):
        if j == 0 or j == i :
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
            
result = 0
cnt = 1

for i in range(r-1,limit):
    result += sum(dp[i][c-1:c+cnt-1])
    cnt+=1
    
print(result)