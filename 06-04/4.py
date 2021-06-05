#https://www.acmicpc.net/problem/20667
#백준 20667번 크롬(dp)
#import sys
#input = sys.stdin.readline
from collections import deque

n, m, k = map(int, input().split())
result = [int(1e9)]*3
dp=[[0]*(5*n+1) for _ in range(m+1)]
info = deque()
for _ in range(n):
    cpu, mem, pri = map(int, input().split())
    info.append([cpu, mem, pri])
    dp[cpu][pri] = mem
    
memCheck = False
cpuCheck = False