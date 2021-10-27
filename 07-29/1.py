#https://www.acmicpc.net/problem/18311
#백준 18311번 왕복 (그리디)
#import sys
#input = sys.stdin.readline

n, k = map(int, input().split())

courses = list(map(int, input().split()))

for i in range(n*2):
    target = i
    if i >= n :
        target = 2*n-1-i
    k -= courses[target]
    if k < 0 :
        print(target+1)
        break