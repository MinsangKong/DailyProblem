#https://www.acmicpc.net/problem/6236
#백준 6236번 용돈 관리(이분탐색)
#import sys
#input = sys.stdin.readline

n, m = map(int, input().split())

costs = [int(input()) for _ in range(n)]

left = max(costs)
right = sum(costs)
result = int(1e9)

while left <= right:
    mid = (left+right)//2
    cnt = 1
    point = mid
    for cost in costs:
        if point-cost >= 0:
            point-=cost
        else:
            cnt+=1
            point = mid-cost

    if cnt <= m:
        result = mid
        right = mid-1
    else:
        left = mid+1
        
print(result)