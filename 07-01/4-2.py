#https://www.acmicpc.net/problem/10942
#백준 10942번 팰린드롬?(DP)
#import sys
#input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

dp = [[0]*n for _ in range(n)]

for i in range(n):
    dp[i][i] = 1
    
for i in range(n-1):
    if nums[i] == nums[i+1]:
        dp[i][i+1] = 1

for k in range(2,n):
    for i in range(n-k):
        j = i+k
        if nums[i] == nums[j] and dp[i+1][j-1]:
            dp[i][j] = 1

m = int(input())

for _ in range(m):
    s,e = map(int, input().split())
    print(dp[s-1][e-1])
    
#처음에 작성한 방식도 맞는 방법이었다... 
#처리할 때 for문의 값을 잘 못 처리해서 계속 틀렸었다...