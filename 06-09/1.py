#https://www.acmicpc.net/problem/7568
#백준 7568번 덩치(정렬)
#import sys
#input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
result = []
for i in arr:
    cnt = 1
    w = i[0]
    h = i[1]
    for j in arr:
        if w < j[0] and h < j[1]:
            cnt+=1
    result.append(cnt)
    
print(*result)