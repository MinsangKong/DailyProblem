#https://www.acmicpc.net/problem/11687
#백준 11687번 팩토리얼 0의 개수(수학,이분탐색)
#import sys
#input = sys.stdin.readline
def pow(n):
    r = 0
    while n:
        r+=n//5
        n//=5
    return r

m = int(input())

start, end = 0, 10**9

result = 0
while start <= end:
    mid = (start+end)//2
    if pow(mid) >= m:
        result = mid
        end = mid-1
    else:
        start = mid +1
        
if pow(result) == m:
    print(result)
else:
    print(-1)