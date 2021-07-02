#https://www.acmicpc.net/problem/19645
#백준 19645번 햄최몇?(이분탐색)
#import sys
#input = sys.stdin.readline

n = int(input())

values = sorted(list(map(int, input().split())), reverse = True)

left = 1
right = sum(values)
result = 0

print(values)
while left <= right:
    mid = (left+right) // 2
    cnt = 0
    total = 0
    for value in values:
        total += value
        if total >= mid:
            cnt += 1
            total = 0
    if cnt >= 3:
        result = mid
        left = mid+1
    else:
        right = mid-1
print(result)
'''
이분 탐색으로는 답을 구할 수 없었다...
'''