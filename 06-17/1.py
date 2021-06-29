#https://www.acmicpc.net/problem/10974
#백준 10974번 모든 순열(그리디)
#import sys
#input = sys.stdin.readline
from itertools import permutations

n = int(input())
arr = [i+1 for i in range(n)]

for i in permutations(arr,n):
    print(*i)