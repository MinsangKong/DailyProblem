#https://www.acmicpc.net/problem/1182
#백준 1182번 부분수열의 합(DFS)
#import sys
#input = sys.stdin.readline

def dfs(total, i):
    if i >= n:
        if total == s :
            global cnt
            cnt+=1
        return
    dfs(total,i+1)
    dfs(total+nums[i],i+1)

n, s = map(int, input().split())

nums = sorted(list(map(int, input().split())))

cnt = 0

dfs(0,0)

if s == 0:
    cnt-=1
    
print(cnt)