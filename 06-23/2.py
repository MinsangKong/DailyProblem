#https://www.acmicpc.net/problem/2961
#백준 2961번 도영이가 만든 맛있는 음식(DFS)
#import sys
#input = sys.stdin.readline

def dfs(x,y,node,length):
    global result
    if length == n:
        if x != 0 and y != 0:
            result = min(result, abs(x-y))
        return
    else:
        if x == 0:
            dfs(info[node][0],y+info[node][1],node+1,length+1)
        else:
            dfs(info[node][0]*x,y+info[node][1],node+1,length+1)
        dfs(x,y,node+1,length+1)

n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]
result = int(1e9)

dfs(0,0,0,0)
print(result)