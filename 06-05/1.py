#https://www.acmicpc.net/problem/1668
#백준 1668번 트로피 진열(그리디)
#import sys
#input = sys.stdin.readline

n = int(input())

trophy = [int(input()) for _ in range(n)]

left = 0
leftCnt = 0
right = 0
rightCnt = 0

for i in range(n):
    if left < trophy[i]:
        left = trophy[i]
        leftCnt+=1
        
for i in range(n-1,-1,-1):
    if right < trophy[i]:
        right = trophy[i]
        rightCnt+=1
        
print(leftCnt)
print(rightCnt)