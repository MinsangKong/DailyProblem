#https://www.acmicpc.net/problem/11066
#백준 11066번 파일 합치기 3 (DP)
import sys
#input = sys.stdin.readline
INF = sys.maxsize

t = int(input())

for _ in range(t):
    n = int(input())
    dp = [[INF]*n for _ in range(n)]
    nums = list(map(int, input().split()))
    for i in range(n):
        dp[i][i] = 0
    for x in range(1,n):
        for i in range(n-x):
            j = i + x
            total = sum(nums[i:j+1])
            for k in range(i,j):
                dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]+total)
    print(dp[0][n-1])
#https://ca.ramel.be/68 참고
#DP를 떠올리기 너무 힘든 문제였다.