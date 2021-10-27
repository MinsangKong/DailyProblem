#https://www.acmicpc.net/problem/9466
#백준 9466번 텀 프로젝트 (DFS)
#import sys
#input = sys.stdin.readline
        
def dfs(idx):
    q = [idx]
    cnt = 1
    ways = dict()
    ways[idx] = 0
    visited[idx] = 1
    flag = True
    while q :
        now = q.pop()
            
        if nums[now] == -1 :
            break
        if nums[now] == now :
            cnt -= 1
            break
        if nums[now] in ways :
            cnt = ways[nums[now]]
            break
        
        if not visited[nums[now]]:
            visited[nums[now]] = 1
            q.append(nums[now])
            ways[nums[now]] = cnt
            cnt += 1
            
    for way in ways :
        nums[way] = -1
    return cnt

t = int(input())

for _ in range(t):
    n = int(input())
    nums = [0]+list(map(int, input().split()))
    visited = [0]*(n+1)          
    result = 0
    
    for i in range(1,n+1):
        if not visited[i]:
            result += dfs(i)            
    print(result)