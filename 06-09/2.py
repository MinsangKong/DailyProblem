#https://www.acmicpc.net/problem/6603
#백준 6603번 로또(정렬,조합)
#import sys
#input = sys.stdin.readline
from itertools import combinations


while True:
    nums = list(map(int, input().split()))
    if nums[0] == 0:
        break
    lotto = combinations(nums[1:],6)
    result = sorted(lotto)
    for i in result:
        print(*i)
    print()