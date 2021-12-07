#https://www.acmicpc.net/problem/14627
#백준 14627번 파닭파닭 (이분탐색)
#import sys
#input = sys.stdin.readline

s,c = map(int, input().split())
nums = [int(input()) for _ in range(s)]
s = 1
e = max(nums)
result = 0

while s <= e :
    mid = (s+e)//2
    cnt = 0
    
    for num in nums:
        cnt += num//mid
        
    if cnt < c :
        e = mid - 1
    else:
        s = mid + 1
        result = mid

print(sum(nums)-c*result)