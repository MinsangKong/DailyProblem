#https://www.acmicpc.net/problem/2304
#백준 2304번 창고 다각형(구현)
#import sys
#input = sys.stdin.readline

n = int(input())

l = 1000
r = l
lineMax=0
lineIdx=0
info = []

for _ in range(n):
    idx, height = map(int, input().split())
    info.append([idx, height])
    if l > idx:
        l = idx
    if l > r:
        r = idx
    if height > lineMax:
        lineMax = height
        lineIdx = idx
        
heights = [0]*(r+1)
for idx, height in info:
    heights[idx]=height
    
size = 0
total = 0
for i in range(lineIdx+1):
    if heights[i] > size:
        size = heights[i]
    total += size
    
size = 0
for i in range(r,lineIdx,-1):
    if heights[i] > size:
        size = heights[i]
    total += size
    
print(total)
'''
높이 배열을 구하고 매 칸마다 넓이를 구하는 방식으로 했더니 문제 없이 구해진다.
아직도 위의 예의 반례를 모르겠다...
'''
7