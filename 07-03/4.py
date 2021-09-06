#https://www.acmicpc.net/problem/1300
#백준 1300번 k번째 수(이분탐색)
#import sys
#input = sys.stdin.readline

n = int(input())
k = int(input())

s, e = 1, k
result = 0

while s <= e:
    mid = (s+e)//2
    temp = 0
    for i in range(1,n+1):
        temp += min(n, mid//i) #mid보다 작은 숫자의 갯수
    if temp < k:
        s = mid+1
    else:
        e = mid-1
        result = mid
        
print(result)