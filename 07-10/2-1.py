#https://www.acmicpc.net/problem/15665
#백준 15665번 N과 M(11) (DFS)
#import sys
#input = sys.stdin.readline

def dfs(depth, num):
    if depth == 0 :
        if num not in result:
            result[num] = 1
            print(num)
        return
    for node in nums:
        dfs(depth-1, num+str(node)+" ")
    
n, m = map(int, input().split())

nums = sorted(set(map(int, input().split())))

result = dict()

dfs(m, "")