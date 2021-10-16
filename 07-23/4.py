#https://www.acmicpc.net/problem/11049
#백준 11049번 행렬 곱셈 순서(DP)
#import sys
#input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

for i in range(1,n): #몇 번째 대각선인가?
    for j in range(0,n-i): #대각선에서 몇 번째 열인가?
        if i == 1: #차이가 1밖에 나지 않는 칸이기 때문에 주변 열을 기준으로 구함
            dp[j][j+i] = data[j][0]*data[j][1]*data[j+i][1]
            continue
        dp[j][j+i] = 2**31
        for k in range(j,j+i):
            dp[j][j+i] = min(dp[j][j+i],
                             dp[j][k]+dp[k+1][j+i]+data[j][0]*data[k][1]*data[j+i][1])
            
print(dp[0][n-1]) #맨 오른쪽 위
'''
https://claude-u.tistory.com/271 참고,
행렬이 채워지는 순서는 아래와 같다. n이 4일 때,
dp[0][1] -> dp[1][2] -> dp[2][3] -> dp[0][2] -> dp[1][3] -> dp[0][3]
'''