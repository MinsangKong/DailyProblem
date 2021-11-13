#https://www.acmicpc.net/problem/11509
#백준 11509번 풍선 맞추기 (자료구조)
#import sys
#input = sys.stdin.readline
from collections import defaultdict

n = int(input())
balloons = list(map(int, input().split()))

result = 0
arrows = defaultdict(int)

for i in range(n):
    if arrows[balloons[i]] > 0 :
        arrows[balloons[i]] -= 1
        arrows[balloons[i]-1] += 1
    else:
        result += 1
        arrows[balloons[i]-1] += 1
        
print(result)