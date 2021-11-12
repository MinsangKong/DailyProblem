#https://www.acmicpc.net/problem/15810
#백준 15810번 풍선 공장 (파라매트릭 서치, lower bound)
#import sys
#input = sys.stdin.readline 

n , m = map(int, input().split()) 
arr = list(map(int, input().split()))
    
s = min(arr)
e = min(arr)*m
while s < e:
    mid = (s+e)//2
    total = 0
    for i in arr:
        total += (mid//i)
        
    if total < m:
        s = mid + 1
    else :
        e = mid
print(s)