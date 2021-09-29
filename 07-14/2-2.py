#https://www.acmicpc.net/problem/4811
#백준 4811번 알약(DP)
#import sys
#input = sys.stdin.readline

dp = [[0]*31 for _ in range(31)] # i => H의 횟수, j => W의 횟수
    
for i in range(31):
    dp[0][i] = 1 #알약 한개를 완전히 먹음(H가 없음)
    
for i in range(1,31):
    for j in range(i,31):
        dp[i][j] = dp[i-1][j]+dp[i][j-1]

while True:
    n = int(input())
    if n == 0 :
        break
    print(dp[n][n])
    
'''
간단하게 생각하면 half의 수, 일반 알약의 수를 기준으로 dp를 만들고
모두 half만 남은 경우에는 경우의 수가 1가지이기 때문에 1로 저장한다.
이 후, dp를 처리할 때 일반 알약을 쪼개야만 half의 수가 늘어나기 때문에 결국
W의 횟수보다 H의 횟수는 작거나 같아야 한다.
'''