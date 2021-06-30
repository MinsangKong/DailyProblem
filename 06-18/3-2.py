#https://www.acmicpc.net/problem/17610
#백준 17610번 양팔 저울(DFS)
#import sys
#input = sys.stdin.readline
def dfs(node, cost):
    global result
    if node == n:
        if 0 < cost <= total:
            result.add(cost)
    else:
        dfs(node+1,cost+nums[node])
        dfs(node+1,cost-nums[node])
        dfs(node+1,cost)

n = int(input())
nums = sorted(list(map(int, input().split())))
total = sum(nums)
result = set()

dfs(0,0)

print(total - len(result))
'''
2중 for문으로 백트래킹을 하는 방식은 시간초과가 발생하고 단순하게 경우의 수를 
+,0,-로 나누어서 dfs를 하는 방식은 문제없이 가능했다.
한 번 틀리니까 다른 방법이 안 떠올라서 계속 해멨다...
'''