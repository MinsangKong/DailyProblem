#https://www.acmicpc.net/problem/16194
#백준 16194번 카드 구매하기 2 (DP)
#import sys
#input = sys.stdin.readline

n = int(input())
cards = [0]+list(map(int, input().split()))

dp = cards[:]

for i in range(1,n+1):
    for j in range(1,i):
        dp[i] = min(dp[i], dp[i-j]+dp[j])
        
print(dp[n])
# 2중 for문이라서 속도가 조금 느리다.