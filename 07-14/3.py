#https://www.acmicpc.net/problem/14719
#백준 14719번 빗물(구현)
#import sys
#input = sys.stdin.readline

h, w = map(int, input().split())
heights = list(map(int, input().split()))

result = 0

target = heights.index(max(heights))

l = r = 0
for i in range(target):
    if heights[i] > l :
        l = heights[i]
    else:
        result += l-heights[i]
        
for i in range(w-1,target,-1):
    if heights[i] > r :
        r = heights[i]
    else:
        result += r-heights[i]
        
print(result)