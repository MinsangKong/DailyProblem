#https://www.acmicpc.net/problem/16432
#백준 16432번 떡장수와 호랑이 (DFS, 백트래킹)
import sys
#input = sys.stdin.readline

def dfs(idx, tteoks):
    if idx == n :
        for day in tteoks :
            print(day)
        sys.exit(0)
    if idx == 0 :
        for num in nums[idx][1:]:
            tteoks.append(num)
            dfs(idx+1,tteoks)
            tteoks.pop() 
    else:
        for num in nums[idx][1:]:
            if tteoks[-1] != num :
                tteoks.append(num)
                dfs(idx+1,tteoks)
                tteoks.pop()

n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]
dfs(0,[])
print(-1)
#시간 초과 발생. 실패했던 부분도 다시 방문했기 때문