#https://www.acmicpc.net/problem/5624
#백준 5624번 좋은 수 (DP)
#import sys
#input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
book = set()
book.add(nums[0]+nums[0])
cnt = 0

for i in range(1,n):
    for j in range(i):
        if nums[i]-nums[j] in book:
            cnt += 1
            break
    for j in range(i+1):
        book.add(nums[i]+nums[j])
    
print(cnt)