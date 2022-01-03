#https://www.acmicpc.net/problem/18353
#백준 18353번 병사 배치하기 (이분탐색)
#import sys
#input = sys.stdin.readline
import bisect

n = int(input())
solders = list(map(int, input().split()))
dp = [solders[-1]]

for i in range(n-2,-1,-1):
    if dp[-1] < solders[i]:
        dp.append(solders[i])
    else:
        dp[bisect.bisect_left(dp,solders[i])] = solders[i]
        
print(n-len(dp))