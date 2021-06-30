#https://www.acmicpc.net/problem/17610
#백준 17610번 양팔 저울(DFS)
#import sys
#input = sys.stdin.readline

def dfs(num):
    result[num] += 1
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            dfs(num+nums[i])
            if num > nums[i]:
                dfs(num-nums[i])
            visited[i] = 0

n = int(input())
nums = sorted(list(map(int, input().split())))
total = sum(nums)
result = [0]*(total+1)
visited = [0]*n

dfs(0)
cnt = 0
for i in result:
    if i == 0:
        cnt+=1
print(cnt)

'''
dfs로 백트래킹을 하며 완전 탐색 하는 방식은 시간초과 발생
'''