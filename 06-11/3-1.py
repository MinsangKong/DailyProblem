#https://www.acmicpc.net/problem/18866
#백준 18866번 젊은 날의 생이여(부분합)
#import sys
#input = sys.stdin.readline

n = int(input())

info = [[0]*2 for _ in range(n)]

for i in range(n):
    a,b = map(int, input().split())
    info[i][0] = a
    info[i][1] = b
    
young = [[0]*2 for _ in range(n)]
old = [[0]*2 for _ in range(n)]

minHappy = int(1e9)
maxTired = -1
maxHappy = -1
minTired = int(1e9)

for i in range(n):
    if info[i][0] != 0 :
        minHappy = min(minHappy, info[i][0])
    if info[i][1] != 0:
        maxTired = max(maxTired, info[i][1])
    young[i][0] = minHappy
    young[i][1] = maxTired

for i in range(n-1,-1,-1):
    if info[i][0] != 0 :
        maxHappy = max(maxHappy, info[i][0])
    if info[i][1] != 0:
        minTired = min(minTired, info[i][1])
    old[i][0] = maxHappy
    old[i][1] = minTired
            
result = -1

for i in range(n-2,-1,-1):
    if young[i][0] > old[i+1][0] and young[i][1] < old[i+1][1]:
        result = i+1
        break
        
print(result)