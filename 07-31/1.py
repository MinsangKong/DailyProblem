#https://www.acmicpc.net/problem/1158
#백준 1158번 요세푸스 문제(자료구조)
#import sys
#input = sys.stdin.readline

n , k = map(int, input().split())

arr = [i for i in range(n)]

result = []
num = 0
for i in range(n):
    num += k-1
    if num >= len(arr):
        num = num%len(arr)
        
    result.append(arr.pop(num))
    
print("<", end ="")
for i in range(n):
    if i == n-1:
        print(result[i]+1,end=">")
    else:
        print(result[i]+1, end=", ")