#https://www.acmicpc.net/problem/13975
#백준 13975번 파일 합치기 3(heap)
#import sys
#input = sys.stdin.readline
import heapq

t = int(input())

for _ in range(t):
    k = int(input())
    files = sorted(list(map(int, input().split())))
    total = 0

    while len(files) >= 2:
        file1 = heapq.heappop(files)
        file2 = heapq.heappop(files)
        cost = file1+file2
        heapq.heappush(files,cost)
        total+=cost
    print(total)
    