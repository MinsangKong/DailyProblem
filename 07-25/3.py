#https://www.acmicpc.net/problem/21278
#백준 21278번 호석이 두 마리 치킨 (플로이드)
#import sys
#input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())
graph = [[101]*n for _ in range(n)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1
    
for i in range(n):
    graph[i][i] = 0
    
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

left = 0
right = 0
result = 101*n
check = [i for i in range(n)]
for a,b in combinations(check,2):
    total = 0
    for i in range(n):
        total += min(graph[i][a]+graph[a][i],graph[i][b]+graph[b][i])
        
    if result > total:
        result = total
        if a > b:
            left, right = b,a
        else:
            left, right = a,b
    elif result == total:
        if min(a,b) < left :
            left = min(a,b)
            right = max(a,b)
        elif min(a,b) == left and max(a,b) < right:
            right = max(a,b)
            
print(left+1,right+1,result)