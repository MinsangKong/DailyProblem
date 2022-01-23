#https://www.acmicpc.net/problem/2635
#백준 2635번 수 이어가기 (정수론)
#import sys
#inpnut = sys.stdin.readline

n = int(input())
result = []
cnt = 0

for i in range(1,30001):
    temp = [n,i]
    while True:
        if temp[-2]-temp[-1] < 0 :
            break
        temp.append(temp[-2]-temp[-1])
    if len(temp) > cnt :
        result = temp
        cnt = len(temp)
        
print(cnt)
print(*result)