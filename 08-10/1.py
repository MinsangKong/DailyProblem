#https://www.acmicpc.net/problem/1439
#백준 1439번 뒤집기(그리디)
#import sys
#input = sys.stdin.readline

def count(target):
    cnt = 0
    for i in range(1,length):
        if nums[i] != nums[i-1]:
            if nums[i-1] != target:
                cnt += 1
    if nums[-1] != target:
        cnt += 1
    return cnt

nums = list(input().rstrip())
length = len(nums)
one2zero = count('0')
zero2one = count('1')

print(min(one2zero, zero2one))