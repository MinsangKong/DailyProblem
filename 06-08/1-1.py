#https://www.acmicpc.net/problem/2231
#백준 2231번 분해합(그리디)
#import sys
#input = sys.stdin.readline

n = int(input())

result = 0
for i in range(1,n+1):
    num = i
    check = str(i)
    for j in check:
        num+=int(j)
    if num == n :
        result = i
        break
        
print(result)