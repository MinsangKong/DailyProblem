#https://www.acmicpc.net/problem/14728
#백준 14728번 벼락치기(DFS, 백트래킹)
#import sys
#input = sys.stdin.readline

def dfs(idx, time, score):
    global result
    if idx == n :
        result = max(result, score)
        return
    if time + info[idx][0] <= t :
        dfs(idx+1,time+info[idx][0], score+info[idx][1])
    dfs(idx+1,time,score)

n, t = map(int, input().split())

info = sorted([list(map(int, input().split())) for _ in range(n)])

result = 0 

dfs(0,0,0)

print(result)
#완전 탐색 방식은 시간초과 발생