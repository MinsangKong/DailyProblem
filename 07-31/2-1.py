#https://www.acmicpc.net/problem/11052
#백준 11052번 카드 구매하기 (DP)
#import sys
#input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
dp = [0]*(n+1)

for i in range(1,n+1):
    dp[i] = cards[i-1]
    for j in range(1,i):
        dp[i] = max(dp[i],dp[i-j]+cards[j-1])
        
print(dp[n])