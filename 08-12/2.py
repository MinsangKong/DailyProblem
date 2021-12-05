#https://www.acmicpc.net/problem/11265
#백준 11265번 끝나지 않는 파티 (플로이드)
#import sys
#input = sys.stdin.readline

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
partys = [list(map(int, input().split())) for _ in range(n)]
    
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j :
                continue
            partys[i][j] = min(partys[i][j], partys[i][k]+partys[k][j])
    
for _ in range(m):
    start, end, cost = map(int, input().split())
    result = partys[start-1][end-1]
    if cost >= result:
        print("Enjoy other party")
    else:
        print("Stay here")