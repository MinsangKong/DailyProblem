#https://www.acmicpc.net/problem/16206
#백준 16206번 롤케이크 (그리디, 정렬)
#import sys
#input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
best = []
normal = []

for i in range(n):
    if nums[i]%10 == 0 :
        best.append(nums[i])
    else:
        normal.append(nums[i])
        
cakes = sorted(best)+normal
result = 0

for i in range(n):
    if cakes[i] == 10 :
        result += 1
        continue
    cake = cakes[i]
    while cake >= 10 :
        if cake == 10 :
            result += 1
            break
        if m == 0 :
            break
        m -= 1
        cake -= 10
        result += 1
        
print(result)