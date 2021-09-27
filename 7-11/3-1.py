#https://www.acmicpc.net/problem/13422
#백준 13422번 도둑(완전탐색)
#import sys
#input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())
    nums = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        s = i
        e = i+m
        if e <= n:
            if sum(nums[s:e]) < k:
                cnt += 1
        else:
            if sum(nums[s:])+sum(nums[:e-n]) < k :
                cnt += 1
                
    print(cnt)
#완전탐색 방식은 시간초과 발생