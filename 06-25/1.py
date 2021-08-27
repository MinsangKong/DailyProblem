#https://www.acmicpc.net/problem/14247
#백준 14247번 나무 자르기(정렬, 그리디)
#import sys
#input = sys.stdin.readline

n = int(input())
hi = list(map(int, input().split()))
ai = list(map(int, input().split()))
result=[]
for i in range(n):
    result.append([hi[i],ai[i]])
l = lambda x: x[1]
result = sorted(result, key = l)
cost = 0
for i in range(n):
    cost += result[i][0]+result[i][1]*i
    
print(cost)