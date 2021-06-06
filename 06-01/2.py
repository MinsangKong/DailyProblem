#https://www.acmicpc.net/problem/11000
#백준 11000번 강의실 배정(정렬)
#import sys
#input = sys.stdin.readline
import heapq

n = int(input())
classes = []

for _ in range(n):
    classes.append(list(map(int, input().split())))
    
classes.sort(key = lambda x : (x[0],x[1]))

cnt = 1
lesson = []
heapq.heappush(lesson, classes[0][1])

for i in range(1,n):
    start, end = classes[i]
    if start >= lesson[0]:
        heapq.heappop(lesson)
    else:
        cnt+=1
    heapq.heappush(lesson, end)
        