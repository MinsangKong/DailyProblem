#https://www.acmicpc.net/problem/2696
#백준 2696번 중앙값 구하기 (자료구조)
#import sys
#input = sys.stdin.readline
import heapq

t = int(input())

for _ in range(t):
    n = int(input())
    nums = []
    temp = n
    while temp > 0 :
        data = list(map(int, input().split()))
        nums.extend(data)
        temp -= 10
    result = []
    maxheap = []
    minheap = []
    
    for i in range(n):
        if len(maxheap) != len(minheap):
            heapq.heappush(minheap,nums[i])
        else:
            heapq.heappush(maxheap,-nums[i])
        
        if minheap :
            while minheap[0] < -maxheap[0]:
                minnum = heapq.heappop(minheap)
                maxnum = heapq.heappop(maxheap)
                heapq.heappush(minheap,-maxnum)
                heapq.heappush(maxheap,-minnum)
            
        if i%2 == 0 :
            result.append(-maxheap[0])
            
    cnt = 0
    print(len(result))
    while cnt < len(result) :
        if cnt+10 > len(result):
            print(*result[cnt:len(result)])
        else:
            print(*result[cnt: cnt+10])
        cnt += 10