#https://www.acmicpc.net/problem/20440
#백준 20440번 검색 🎵니가 싫어 싫어 너무 싫어 싫어 오지 마 내게 찝쩍대지마🎵 - 1(정렬, 누적합)
#import sys
#input = sys.stdin.readline
import heapq

n = int(input())

times = []

for _ in range(n):
    times.append(list(map(int, input().split())))
    
rooms = []
times.sort(key = lambda x : (x[0],x[1]))

cnt = 0
start,end = 0,0
for i in range(n):
    heapq.heappush(rooms, times[i][1])
    point = -1
    
    while times[i][0] >= rooms[0]:
        point = heapq.heappop(rooms)
    
    if len(rooms) > cnt:
        start = times[i][0]
        end = rooms[0]
        cnt = len(rooms)
    elif len(rooms) == cnt and point == times[i][0]:
        end = rooms[0]
        
print(cnt)
print(start,end)