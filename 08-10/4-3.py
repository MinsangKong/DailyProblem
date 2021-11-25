#https://www.acmicpc.net/problem/11066
#백준 11066번 파일 합치기 3 (DP,Knuth's Optimization)
import sys
#input = sys.stdin.readline
INF = sys.maxsize

t = int(input())

for _ in range(t):
    n = int(input())
    dp = [[INF]*n for _ in range(n)]
    knuth = [[0]*n for _ in range(n)]
    prefix = [0]*(n+1)
    nums = list(map(int, input().split()))
    for i in range(n):
        dp[i][i] = 0
        prefix[i+1] = prefix[i]+nums[i]
        knuth[i][i] = i
    for x in range(1,n):
        for i in range(n-x):
            j = i + x
            total = prefix[j+1] - prefix[i]
            for k in range(knuth[i][j-1],knuth[i+1][j]+1):
                if k < n-1 and dp[i][j] > dp[i][k]+dp[k+1][j] + total:
                    dp[i][j] = dp[i][k]+dp[k+1][j]+total
                    knuth[i][j] = k
    print(dp[0][n-1])
'''
https://ca.ramel.be/68를 보면 
1. DP 점화식의 꼴

2. 사각부등식

3. 단조성

를 만족하면 knuth[i][j-1] <= knuth[i][j] <= knuth[i+1][j]+1로 범위를 제한해서
O(N^3) 문제를 O(N^2)의 문제로 최적화 할 수 있다.
'''