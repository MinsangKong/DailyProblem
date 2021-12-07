#https://www.acmicpc.net/problem/11568
#백준 11568번 민균이의 계략 (이분탐색)
#import sys
#input = sys.stdin.readline
import bisect

n = int(input())
nums = list(map(int, input().split()))

sub = [nums[0]]

for i in range(1,n):
    if sub[-1] < nums[i]:
        sub.append(nums[i])
    else:
        sub[bisect.bisect_left(sub,nums[i])]=nums[i]
    
print(len(sub))