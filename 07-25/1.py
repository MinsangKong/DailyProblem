#https://www.acmicpc.net/problem/1010
#백준 1010번 다리 놓기 (정수론)
#import sys
#input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a,b = map(int, input().split())
    if a < b :
        a,b = b,a
    d = 1
    for i in range(a,a-b,-1):
        d *= i
    m = 1
    for i in range(1,b+1):
        m *= i
    print(d//m)