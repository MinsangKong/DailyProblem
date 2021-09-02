#https://www.acmicpc.net/problem/18258
#백준 18258번 큐 2(자료구조)
#import sys
#input = sys.stdin.readline
from collections import deque

q = deque()

for _ in range(int(input())):
    oper = list(input().split())
    if oper[0] == 'push':
        q.append(oper[1])
    elif oper[0] == 'pop':
        if q :
            print(q.popleft())
        else:
            print(-1)
    elif oper[0] == 'size':
        print(len(q))
    elif oper[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif oper[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif oper[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)