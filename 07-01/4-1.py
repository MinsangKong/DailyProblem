#https://www.acmicpc.net/problem/10942
#백준 10942번 팰린드롬?(DP)
#import sys
#input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

dp = [[0]*n for _ in range(n)]

for k in range(n):
    for i in range(n):
        j = i+k
        if j >= n:
            break
        if i == j:
            dp[i][j] = 1
            continue
        if i+1 == j and nums[i] == nums[j]:
            dp[i][j] = 1
            continue
        if nums[i] == nums[j] and dp[i+1][j-1]:
            dp[i][j] = 1

m = int(input())

for _ in range(m):
    s,e = map(int, input().split())
    print(dp[s-1][e-1])
'''
계속 틀려서 구글링해서 작성한 결과 범위 조절을 잘 못했다.
n - 7일때 dp를 만들면 아래처럼 for문을 작성했어야 했다.

1, 2, 3, 4, 5, 6, 7

(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7)

(1, 3), (2, 4), (3, 5), (4, 6), (5, 7)

(1, 4), (2, 5), (3, 6), (4, 7)

(1, 5), (2, 6), (3, 7)

(1, 6), (2, 7)

(1, 7)
'''