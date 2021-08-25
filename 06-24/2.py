#https://www.acmicpc.net/problem/13549
#백준 13549번 숨바꼭질 5(다익스트라)
#import sys
#input =sys.stdin.readline
import heapq
INF = int(1e9)
def dijkstra(n,k):
    board[n] = 0
    q = []
    heapq.heappush(q,(0,n))
    while q:
        sec, now = heapq.heappop(q)
        if now == k:
            return sec
        if now == 0:
            if board[now+1] > sec+1:
                board[now+1] = sec+1
                heapq.heappush(q,(sec+1,now+1))
        elif now == 100000:
            if board[now-1] > sec+1:
                board[now-1] = sec+1
                heapq.heappush(q,(sec+1,now-1))
        else:
            if board[now-1] > sec+1:
                board[now-1] = sec+1
                heapq.heappush(q,(sec+1,now-1))
            if board[now+1] > sec+1:
                board[now+1] = sec+1
                heapq.heappush(q,(sec+1,now+1))
        if now != 0 and now*2 <= 100000:
            if board[now*2] > sec:
                board[now*2] = sec
                heapq.heappush(q,(sec, now*2))
            

n, k = map(int, input().split())
board = [INF]*100001
print(dijkstra(n,k))