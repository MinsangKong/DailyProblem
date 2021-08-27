#https://www.acmicpc.net/problem/2304
#백준 2304번 창고 다각형(구현)
#import sys
#input = sys.stdin.readline

n = int(input())

info = sorted([list(map(int, input().split())) for _ in range(n)], key = lambda x : x[0])

leftSize = 0
rightSize = 0
base = 0
idx = 0

lineMax = 0
lineIdx = 0
l = r = 0

for i in range(n):
    if lineMax < info[i][1]:
        lineMax = info[i][1]
        l = info[i][0]
        r = info[i][0]+1
        lineIdx = i
        
for i in range(lineIdx):
    if base < info[i][1]:
        if i > 0:
            leftSize+=base*(info[i][0]-idx)
        base = info[i][1]
        idx = info[i][0]
    
    if i == lineIdx-1:
        leftSize += base*(l-idx)
        
base = idx = 0

for i in range(n-1,lineIdx,-1):
    if base < info[i][1]:
        if i != n-1:
            rightSize+=base*(idx-info[i][0])
        base = info[i][1]
        idx = info[i][0]
    
    if i == lineIdx+1:
        rightSize += base*(idx-r) 

if n > 1 and lineIdx != n-1 :
    rightSize+=info[-1][1]
print(leftSize,lineMax,rightSize)
#반례를 못찾겠다... 3가지 기준을 나눠서 구하는 방법은 에러 발생
#하나인 경우, 왼쪽이 가장 큰 경우, 오른쪽이 가장 큰 경우 나눠서 생각했는데 실수가 있는것 같다
7