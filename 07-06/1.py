#https://www.acmicpc.net/problem/14494
#백준 14494번 수리고 항승(그리디)
#import sys
#input = sys.stdin.readline

n, l = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

start = arr[0]
end = arr[0] + l
count = 1
for i in range(n):
    if start <= arr[i] < end:
        continue
    else:
        start = arr[i]
        end = arr[i] + l
        count += 1
print(count)