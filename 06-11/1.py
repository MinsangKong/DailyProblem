#https://www.acmicpc.net/problem/20300
#백준 20300번 서강 근육맨(정렬, 그리디)
#import sys
#input = sys.stdin.readline

n = int(input())
loss = list(map(int, input().split()))

loss.sort()
result = 0

if n == 1:
    print(loss[0])

elif n % 2 == 0:
    start = 0
    end = n-1
    while start < end:
        if loss[start]+loss[end] > result:
            result = loss[start]+loss[end]
        start+=1
        end-=1
    print(result)
else:
    start = 0
    end = n-2
    while start < end:
        if loss[start]+loss[end] > result:
            result = loss[start]+loss[end]
        start+=1
        end-=1
    result = max(result,loss[-1])
    print(result)