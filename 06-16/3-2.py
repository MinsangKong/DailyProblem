#https://www.acmicpc.net/problem/17951
#백준 17951번 흩날리는 시험지 속에서 내 평점이 느껴진거야(이분탐색)
#import sys
#input = sys.stdin.readline

n, k = map(int, input().split())
scores = list(map(int, input().split()))

left = 0
right = sum(scores)
result = 0

while left <= right:
    mid = (left+right)//2
    total = 0
    cnt = 0
    check = int(1e9)
    for i in range(n):
        total+=scores[i]
        if total >= mid:
            cnt+=1
            total = 0
    if cnt >= k:
        result = mid
        left = mid+1
    else:
        right = mid-1        

print(result)