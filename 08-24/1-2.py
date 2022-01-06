#https://www.acmicpc.net/problem/2428
#백준 2428번 표절 (Lower bound)
#import sys
#input = sys.stdin.readline

n = int(input())
nums = sorted(list(map(int, input().split())))
result = 0

for i in range(n):
    s = i
    e = n
    while s < e :
        mid = (s+e)//2
        if nums[i] >= 0.9*nums[mid]:
            s = mid+1
        else:
            e = mid
    result += (e-i-1)
    
print(result)
#그냥 이분탐색보다 lower bound가 100ms정도 더 빨랐다.