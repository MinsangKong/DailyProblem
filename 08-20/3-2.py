#https://www.acmicpc.net/problem/14863
#백준 14863번 서울에서 경산까지 (DP)
#import sys
#input = sys.stdin.readline

n,k = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(k,info[0][0]-1,-1):
    dp[1][i] = info[0][1]
for i in range(k,info[0][2]-1,-1):
    dp[1][i] = max(dp[1][i], info[0][3])

for i in range(1,n):
    wtime, wcost, btime, bcost = info[i]
    for j in range(k):
        if dp[i][j] and j+wtime <= k:
            dp[i+1][j+wtime] = max(dp[i+1][j+wtime],dp[i][j]+wcost)
        if dp[i][j] and j+btime <= k :
            dp[i+1][j+btime] = max(dp[i+1][j+btime],dp[i][j]+bcost)

#print(dp)
print(dp[n][k])  
#bcost와 wcost를 if문으로 한번에 처리해주는 경우가 훨씬 빨랐다 476->1280ms
#그리고 dp 점화식을 [i][j] -> [i+1][j+btime]이 [j][i] -> [j+btime][i+1]이 훨씬 빨랐다