#https://www.acmicpc.net/problem/20546
#백준 20546번 🐜 기적의 매매법 🐜 (그리디)
#import sys
#input = sys.stdin.readline

start = int(input())

graph = list(map(int, input().split()))

bnp = [start,0]
timing = [start,0]

high = 0
low = 0
for i in range(14):
    if bnp[0] >= graph[i]:
        bnp[1] += bnp[0]//graph[i]
        bnp[0] = bnp[0]%graph[i]
    if i != 0:
        if graph[i] > graph[i-1]:
            high += 1
            low = 0
        elif graph[i] < graph[i-1]:
            low += 1
            high = 0
        else:
            low = 0
            high = 0
    if low >= 3:
        timing[1] += timing[0]//graph[i]
        timing[0] = timing[0]%graph[i]
    elif high >= 3:
        timing[0] +=graph[i]*timing[1]
        timing[1] = 0
        
total_bnp = bnp[0]+graph[-1]*bnp[1]
total_timing = timing[0]+graph[-1]*timing[1]

if total_bnp > total_timing:
    print("BNP")
elif total_bnp < total_timing:
    print("TIMING")
else:
    print("SAMESAME")