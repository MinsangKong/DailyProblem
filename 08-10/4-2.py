#https://www.acmicpc.net/problem/11066
#백준 11066번 파일 합치기 3 (DP)
import sys
#input = sys.stdin.readline
INF = sys.maxsize

t = int(input())

for _ in range(t):
    n = int(input())
    dp = [[INF]*n for _ in range(n)]
    prefix = [0]*(n+1)
    nums = list(map(int, input().split()))
    for i in range(n):
        dp[i][i] = 0
        prefix[i+1] = prefix[i]+nums[i]
    for x in range(1,n):
        for i in range(n-x):
            j = i + x
            total = prefix[j+1] - prefix[i]
            for k in range(i,j):
                dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]+total)
    print(dp[0][n-1])
#매번 sum을 하지 않고 누적합 방식으로 바꿨더니 600ms 정도 빨라졌다.