#https://www.acmicpc.net/problem/16472
#백준 16472번 고냥이()
#import sys
#input = sys.stdin.readline
from itertools import combinations

n = int(input())
word = list(input().rstrip())
alpha = list(set(word))
length = len(alpha)

if length <= n:
    print(len(word))
else:
    result = 0
    for comb in combinations(alpha, n):
        count = 0
        for i in range(len(word)):
            if word[i] in comb:
                count+=1
            else:
                result = max(count,result)
                count = 0
    print(result)
#완전 탐색 방식은 시간 초과 발생