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
heapq.heappush(rooms,[times[0][1],times[0][0]])
start,end = times[0][0],times[0][1]
length = 0
for i in range(1, n):
    s, e= times[i][0], times[i][1]
    flag = True
    point = int(1e9)
    if rooms:
        while rooms:
            if rooms[0][0] > s:
                break
            elif rooms[0][0] == s:
                flag = False
                re, rs = heapq.heappop(rooms)
                point = min(rs,point)
            else:
                heapq.heappop(rooms)
    if flag :
        heapq.heappush(rooms,[e,s])
    else:
        heapq.heappush(rooms, [e,point])
    if cnt < len(rooms):
        cnt = len(rooms)
        start = max(rooms[0][1],s)
        end = rooms[0][0]
    elif cnt == len(rooms):
        start = point
        end = rooms[0][0]
                
print(cnt)
print(start,end)

'''
33%에서 계속 틀렸습니다가 나오는데 해결법을 못찾겠다....
결과적으로 먼저 heapq에 값을 넣은 다음 더 이상 작은 수가 없을 때까지 pop을 진행하고
end를 갱신하는 방향으로 풀어야 했다. pop을 먼저하는 방식이여서 틀린것 같다
'''