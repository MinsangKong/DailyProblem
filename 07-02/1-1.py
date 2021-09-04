#https://www.acmicpc.net/problem/14697
#백준 14697번 방 배정하기(자료구조, 브루트포스)
#import sys
#input = sys.stdin.readline
import heapq

a, b, c, n = map(int, input().split())

if n % a == 0 or n % b == 0 or n % c == 0:
    print(1)
else:
    case = [0]*301
    q = []
    
    heapq.heappush(q, a)
    heapq.heappush(q, b)
    heapq.heappush(q, c)
    
    while True:
        num = heapq.heappop(q)
        
        if num > n:
            print(case[n])
            break
            
        if case[num] == 0:
            case[num] = 1
            heapq.heappush(q,num+a)
            heapq.heappush(q,num+b)
            heapq.heappush(q,num+c)
        