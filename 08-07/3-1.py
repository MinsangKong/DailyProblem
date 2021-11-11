#https://www.acmicpc.net/problem/17404
#백준 17404번 RGB 거리 2 (DP)
#import sys
#input = sys.stdin.readline
INF = int(1e9)

n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]
result = INF

dp = [[[0]*2 for _ in range(3)] for _ in range(n-1)]
dp[0][0] = [costs[0][0],1]
dp[0][1] = [costs[0][1],2]
dp[0][2] = [costs[0][2],3]

for i in range(1,n-1):
    for j in range(3):
        a = (j+1)%3
        b = (j+2)%3
        if dp[i-1][a][0] > dp[i-1][b][0]:
            dp[i][j][0] = dp[i-1][b][0]+costs[i][j]
            dp[i][j][1] = dp[i-1][b][1]
        else:
            dp[i][j][0] = dp[i-1][a][0]+costs[i][j]
            dp[i][j][1] = dp[i-1][a][1]

for i in range(3):
    if dp[n-2][i][1] == i+1 :
        result = min(result, dp[n-2][i][0]+min(costs[n-1][(i+1)%3],costs[n-1][(i+2)%3]))
    elif dp[n-2][i][1] == (i+1)%3+1:
        result = min(result, dp[n-2][i][0]+costs[n-1][(i+2)%3])
    else:
        result = min(result, dp[n-2][i][0]+costs[n-1][(i+1)%3])
        
rdp = [[[0]*2 for _ in range(3)] for _ in range(n-1)]
rdp[0][0] = [costs[n-1][0],1]
rdp[0][1] = [costs[n-1][1],2]
rdp[0][2] = [costs[n-1][2],3]

for i in range(1,n-1):
    for j in range(3):
        a = (j+1)%3
        b = (j+2)%3
        if rdp[i-1][a][0] > rdp[i-1][b][0]:
            rdp[i][j][0] = rdp[i-1][b][0]+costs[n-1-i][j]
            rdp[i][j][1] = rdp[i-1][b][1]
        else:
            rdp[i][j][0] = rdp[i-1][a][0]+costs[n-1-i][j]
            rdp[i][j][1] = rdp[i-1][a][1]
for i in range(3):
    if rdp[n-2][i][1] == i+1 :
        result = min(result, rdp[n-2][i][0]+min(costs[0][(i+1)%3],costs[0][(i+2)%3]))
    elif rdp[n-2][i][1] == (i+1)%3+1:
        result = min(result, rdp[n-2][i][0]+costs[0][(i+2)%3])
    else:
        result = min(result, rdp[n-2][i][0]+costs[0][(i+1)%3])
print(result)  
# 탑 다운과 바텀 업을 각각 체크한 뒤 그 둘을 비교하는 방식밖에 안 떠올랐다