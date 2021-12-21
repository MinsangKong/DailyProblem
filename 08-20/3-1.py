#https://www.acmicpc.net/problem/14863
#백준 14863번 서울에서 경산까지 (DP)
#import sys
#input = sys.stdin.readline

def check(time, cost, idx):
    for i in range(k,time-1,-1):
        if dp[i-time][idx-1]:
            dp[i][idx] = max(dp[i][idx],dp[i-time][idx-1]+cost)

n,k = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*n for _ in range(k+1)]

for i in range(k,info[0][0]-1,-1):
    dp[i][0] = info[0][1]
for i in range(k,info[0][2]-1,-1):
    dp[i][0] = max(dp[i][0], info[0][3])

for i in range(1,n):
    wtime, wcost, btime, bcost = info[i]
    check(wtime,wcost,i)
    check(btime,bcost,i)

#print(dp)
print(dp[k][n-1])  