#https://www.acmicpc.net/problem/11279
#백준 11279번 최대 힙(힙)
#import sys
#input = sys.stdin.readline
import heapq

n = int(input())
arr = []

for _ in range(n):
    oper = int(input())
    if oper == 0:
        if arr:
            num = heapq.heappop(arr)
            print(-num)
        else:
            print(0)
    else:
        heapq.heappush(arr,-oper)
        