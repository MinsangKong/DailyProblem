#https://www.acmicpc.net/problem/2422
#백준 2422번 한윤정이 이탈리아에 가서 아이스크림을 사먹는데 (DP)
#import sys
#input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())
dp = [[0]*(n+1) for _ in range(n+1)]
nums = [i for i in range(1,n+1)]
cases = list(combinations(nums,3))
result = 0

for _ in range(m):
    a,b = map(int, input().split())
    dp[a][b] = 1
    dp[b][a] = 1
    
for a,b,c in cases:
    if dp[a][b] or dp[b][c] or dp[a][c]:
        continue
    result += 1
    
print(result)