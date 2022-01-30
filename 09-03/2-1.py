#https://www.acmicpc.net/problem/2876
#백준 2876번 그래픽스 퀴즈 (DP)
#import sys
#input = sys.stdin.readline

n = int(input())
grade = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*6 for _ in range(n)]
dp[0][grade[0][0]] = 1
dp[0][grade[0][1]] = 1
_max = 1
idx = min(grade[0][0],grade[0][1])

for i in range(1,n):
    a,b = grade[i]
    if dp[i-1][a] :
        dp[i][a] = dp[i-1][a]+1
    else:
        dp[i][a] = 1
    if dp[i-1][b]:
        dp[i][b] = dp[i-1][b]+1
    else:
        dp[i][b] = 1
    if dp[i][b] > dp[i][a]:
        cur = b
        cnt = dp[i][b]
    else:
        cur = a
        cnt = dp[i][a]
    if _max < cnt :
        idx = cur
        _max = cnt
    elif _max == cnt and idx > cur:
        idx = cur

print(_max, idx)