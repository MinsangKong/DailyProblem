import sys, heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    graph = [0]+list(map(int,input().split()))
    num = [0 for _ in range(n+1)]
    q = []
    for i in graph:
        num[i] += 1

    for i in range(1,n+1):
        if num[i]==0:
            heapq.heappush(q,i)

    cnt = 0
    while q:
        n = heapq.heappop(q)

        cnt += 1
        num[graph[n]] -= 1
        if num[graph[n]] == 0:
            heapq.heappush(q,graph[n])

    print(cnt)