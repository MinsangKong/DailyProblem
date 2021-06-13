#https://www.acmicpc.net/problem/3151
#백준 3151번 합이 0(투포인터, 정렬)
#import sys
#input = sys.stdin.readline

n = int(input())
spec = list(map(int, input().split()))
cnt = 0

spec.sort()

for i in range(n-2):
    left, right = i+1, n-1
    target = -spec[i]
    idx = n
    while left < right:
        total = spec[left]+spec[right]
        if total < target:
            left+=1
        elif total == target:
            if spec[left] == spec[right]:
                cnt+= right-left
            else:
                if idx > right:
                    idx = right
                    while idx >= 0 and spec[idx-1] == spec[right]:
                        idx-=1
                cnt+=right-idx+1
            left+=1
        else:
            right-=1
            
print(cnt)