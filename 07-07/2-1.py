#https://www.acmicpc.net/problem/11286
#백준 11286번 절댓값 힙(자료구조)
#import sys
#input = sys.stdin.readline
import heapq

n = int(input())

book = dict()
q = []

for _ in range(n):
    num = int(input())
    if num == 0:
        if q:
            target = heapq.heappop(q)
            print(heapq.heappop(book[target]))
        else:
            print(0)
    else:
        target = abs(num)
        heapq.heappush(q, target)
        if target in book:
            heapq.heappush(book[target], num)
        else:
            book[target] = [num]
# 굳이 딕셔너리를 생성하지 않고 -heap과 +heap으로 나눠서 생각했으면 더 빠르게 처리할 수 있었다.