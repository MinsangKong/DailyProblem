#https://www.acmicpc.net/problem/13397
#백준 13397번 구간 나누기 2(이분탐색, 파라매트릭 서치)
#import sys
#input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

start = 0
end = max(nums)-1
result = 0
while start <= end:
    mid = (start+end)//2
    diff_max = nums[0]
    diff_min = nums[0]
    cnt = 1
    for i in range(1,n):
        diff_max = max(diff_max,nums[i])
        diff_min = min(diff_min,nums[i])
        if diff_max - diff_min > mid:
            cnt += 1
            diff_max = nums[i]
            diff_min = nums[i]
    if cnt <= m:
        result = mid
        end = mid-1
    else:
        start = mid+1
        
print(result)