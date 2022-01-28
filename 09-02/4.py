#https://www.acmicpc.net/problem/3673
#백준 3673번 나눌 수 있는 부분 수열 (누적합)
#import sys
#input = sys.stdin.readline
from collections import defaultdict

c = int(input())

for _ in range(c):
    d, n = map(int, input().split())
    counter = defaultdict(int)
    nums = list(map(int, input().split()))
    cnt = 0
    total = 0
    for num in nums:
        total += num
        cnt += counter[total%d]
        counter[total%d] += 1
    print(counter[0]+cnt)