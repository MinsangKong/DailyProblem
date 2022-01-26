#https://www.acmicpc.net/problem/14945
#백준 14945번 불장난 (DP)
#import sys
#input = sys.stdin.readline

n = int(input())
dp = [[0]*(n+1) for _ in range(n+1)] #층수, 둘 사이의 거리
dp[2][1] = 2

for i in range(3,n+1):
    for j in range(1,i):
        dp[i][j] = (dp[i-1][j]*2+dp[i-1][j-1]+dp[i-1][j+1])%10007
        
total = 0
for i in range(1,n):
    total += dp[n][i]
for i in dp:
    print(*i)
print(total%10007)
'''
dp[i-1][j] : 이 전 층과 둘 사이의 거리가 동일 (아래아래, 대각대각)
dp[i-1][j-1] : 이전 층과 둘 사이의 거리가 감소 (대각아래)
dp[i-1][j+1] : 이전 층과 둘 사이의 거리가 증가 (아래대각)
j축을 둘 사이의 거리라고 생각하면 구현하기 쉬웠는데 단순하게 층이라고 생각하니까
엄청 해맷다...
'''