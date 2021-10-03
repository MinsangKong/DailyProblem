#https://www.acmicpc.net/problem/15666
#백준 15666번 N과 M (12) (DFS, 수열)
#import sys
#input = sys.stdin.readline

def dfs(idx, num):
    if len(num) == m :
        key = ' '.join(map(str,num))
        if key not in result:
            print(key)
            result[key] = 1
        return
    for i in range(idx,len(nums)):
        num.append(nums[i])
        dfs(i,num)
        num.pop()

n, m = map(int, input().split())
nums = sorted(set(map(int, input().split())))

result = dict()

dfs(0, [])