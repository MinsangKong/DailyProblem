#https://www.acmicpc.net/problem/1059
#백준 1059번 좋은 구간 (그리디, 정수론)
#import sys
#input = sys.stdin.readline
import bisect

n = int(input())
nums = sorted(list(map(int, input().split())))
num = int(input())
idx = bisect.bisect_left(nums,num)

if num in nums :
    print(0)
elif idx == 0 :
    print((nums[idx]-num)*num-1)
else :
    print((num-nums[idx-1])*(nums[idx]-num)-1)