#https://www.acmicpc.net/problem/21313
#백준 21313번 문어(그리디)
#import sys
#input = sys.stdin.readline

n = int(input())

arr = [[1]*8 for _ in range(n)]
result = []
idx = 0

while True:
    if idx == n-1:
        for i in range(8):
            if arr[idx][i] == 1 and arr[0][i]==1:
                result.append(i+1)
                break
        break
    else:
        for i in range(8):
            if arr[idx][i] == 1 and arr[idx+1][i]==1:
                result.append(i+1)
                arr[idx][i] = 0
                arr[idx+1][i] = 0
                break
        idx+=1
                
print(*result)