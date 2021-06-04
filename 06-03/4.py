#https://www.acmicpc.net/problem/12764
#백준 12764번 싸지방에 간 준하(정렬)
#import sys
#input = sys.stdin.readline
from collections import deque
import heapq

n = int(input())

graph = []

for _ in range(n):
    a,b = map(int, input().split())
    graph.append([a,b])
    
graph.sort(key = lambda x: (x[0],x[1]))
graph = deque(graph)

computers = []
empty = [i for i in range(n)]
heapq.heapify(empty)

check = -1
cnt = [0 for _ in range(n)]
result = [0]

while graph:
    check +=1
    if check==graph[0][0]:
        temp = graph.popleft()
        idx = heapq.heappop(empty)
        heapq.heappush(computers,[temp[1],temp[0],idx])
        cnt[idx]+=1
    if computers and computers[0][0] == check:
        end, start, idx = heapq.heappop(computers)
        heapq.heappush(empty,idx)
        
for i in cnt:
    if i == 0:
        break
    else:
        result.append(i)
        result[0] += 1
        
print(result[0])
print(*result[1:])