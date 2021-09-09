#https://www.acmicpc.net/problem/20167
#백준 20167번 꿈틀꿈틀 호석 애벌레 (DFS)
#import sys
#input = sys.stdin.readline

def dfs(idx, satisfaction, energy):
    global result
    if idx >= n:
        result = max(energy, result)
        return
    if nums[idx] >= k:
        bonus = satisfaction + nums[idx] - k
        dfs(idx+1,0,energy+bonus)
    else:
        if satisfaction + nums[idx] >= k:
            bonus = satisfaction + nums[idx] - k
            dfs(idx+1,0,energy+bonus)
        else:
            dfs(idx+1,satisfaction + nums[idx],energy)
        dfs(idx+1,nums[idx],energy)

n, k = map(int, input().split())
nums = list(map(int, input().split()))
result = 0

dfs(0,0,0)

print(result)
#처음 풀 때에는 입력 받는 수가 k보다 큰 지 확인하지 않았기 때문에 틀렸다고 나왔다.