#https://www.acmicpc.net/problem/18113
#백준 18113번 그르다 김가놈 (이분 탐색)
#import sys
#input = sys.stdin.readline

n, k, m = map(int, input().split())
nums = []

for _ in range(n) :
    num = int(input())
    if num >= 2*k :
        if num-2*k > 0 :
            nums.append(num-2*k)
    elif num > k :
        nums.append(num-k)

result = 0
if nums:
    s = 1
    e = max(nums)
    while s <= e :
        mid = (s+e)//2
        cnt = 0
        for num in nums :
            cnt += num//mid

        if cnt >= m :
            s = mid+1
            result = mid
        else:
            e = mid-1

print(result if result else -1)    