#https://www.acmicpc.net/problem/16432
#백준 16432번 떡장수와 호랑이 (DFS)
import sys
#input = sys.stdin.readline

def dfs(idx, total, last):
    if idx == n :
        for tteok in total :
            print(tteok)
        sys.exit(0)
        
    for num in nums[idx][1:]:
        if last != num and not visited[idx][num] :
            visited[idx][num] = 1
            total.append(num)
            dfs(idx+1,total,num)
            total.pop()

n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*10 for _ in range(n)]
dfs(0,[],-1)
print(-1)
#굳이 방문했던 곳은 visited[idx][num] = 0으로 해줄 필요가 없었다.
#why? 이미 방문한 곳은 실패한 가지이기 때문에 다시 가도 실패할 뿐이다.