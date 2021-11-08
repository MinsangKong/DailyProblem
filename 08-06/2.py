#https://www.acmicpc.net/problem/1469
#백준 1469번 숌 사이 수열 (DFS, 백트래킹)
import sys
#input = sys.stdin.readline

def dfs(count):
    if count == n*2:
        for i in range(n*2):
            print(result[i], end=' ')
        sys.exit(0)
        
    if result[count] != -1 :
        dfs(count+1)
        return
    
    for i in range(n):
        if not visited[i] and count+nums[i]+1 < 2*n and result[count] == -1 and result[count+nums[i]+1] == -1:
            visited[i] = 1
            result[count] = result[count+nums[i]+1] = nums[i]
            dfs(count+1)
            result[count] = result[count+nums[i]+1] = -1
            visited[i] = 0

n = int(input())
nums = sorted(list(map(int, input().split())))
visited = [0]*n
result = [-1]*(2*n)
dfs(0)
print(-1)
'''
순열에서 만족하는 값을 찾으면 빠져나오는 식으로 구하려고 했지만 시간초과가
발생할 것 같아서 백트래킹으로 풀었다.
문제의 포인트는 count와 count+nums[i]+1을 기준으로 백트래킹을 하는 것이다.
이 부분이 안 떠올라서 너무 오래 걸렸다...
'''