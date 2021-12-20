#https://www.acmicpc.net/problem/10653
#백준 10653번 마라톤 2 (DP)
#import sys
#input = sys.stdin.readline
INF = int(1e9)

n, k = map(int, input().split())
checkpoint = [list(map(int, input().split())) for _ in range(n)]
dist = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        dist[i][j] = abs(checkpoint[i][0]-checkpoint[j][0])+abs(checkpoint[i][1]-checkpoint[j][1])
        
dp = [[INF]*n for _ in range(k+1)]
dp[0][0] = 0

for i in range(1,n):
    dp[0][i] = dp[0][i-1]+dist[i-1][i]
    
for i in range(1,k+1):
    dp[i][0], dp[i][1] = 0, dp[i-1][1]
    dp[i][i] = dist[0][i]
    for j in range(1,n):
        for q in range(i,0,-1):
            if j-q-1 < 0 :
                continue
            dp[i][j] = min(dp[i][j], dp[i-q][j-q-1]+dist[j][j-q-1],dp[i][j-1]+dist[j-1][j])
                
#print(dp)
print(dp[k][n-1])
#접근 방식 자체는 맞았지만 갱신하는 과정에서 엄청 헤맸다...