#https://www.acmicpc.net/problem/2798
#백준 2798번 블랙잭(그리디)
#import sys
#input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())

nums = list(map(int, input().split()))

result = 0

for i in combinations(nums, 3):
    total = sum(i)
    if total <= m:
        result = max(total,result)
        
print(result)