#https://www.acmicpc.net/problem/14921
#백준 14921번 용액 합성하기 (투포인터)
import sys
#input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
result = int(1e9)

s = 0
e = n-1

while s < e :
    total = nums[s]+nums[e]
    if abs(result) > abs(total):
        if total == 0:
            print(0)
            sys.exit(0)
        result = total
    if total > 0:
        e -= 1
    else:
        s += 1
print(result) 