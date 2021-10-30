#https://www.acmicpc.net/problem/1655
#백준 1655번 가운데를 말해요 (자료구조)
#import sys
#input = sys.stdin.readline
import heapq

n = int(input())
nums = []
maxheapq = []
minheapq = []

for i in range(n):
    num = int(input())
    
    if len(maxheapq) == len(minheapq):
        heapq.heappush(maxheapq, -num)
    else:
        heapq.heappush(minheapq, num)
        
    if maxheapq and minheapq and -maxheapq[0] > minheapq[0]:
        maxnum = heapq.heappop(maxheapq)
        minnum = heapq.heappop(minheapq)
        heapq.heappush(minheapq, -maxnum)
        heapq.heappush(maxheapq, -minnum)
        
    print(-maxheapq[0])