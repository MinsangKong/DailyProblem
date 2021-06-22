#https://www.acmicpc.net/problem/2309
#백준 2309번 일곱 난쟁이(그리디)
#import sys
#input = sys.stdin.readline
from itertools import combinations

nums = []

for _ in range(9):
    nums.append(int(input()))
    
for i in combinations(nums,7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break