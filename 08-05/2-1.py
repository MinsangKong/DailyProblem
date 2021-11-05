#https://www.acmicpc.net/problem/9489
#백준 9489번 사촌 (트리)
#import sys
#input = sys.stdin.readline

while True:
    n, k = map(int, input().split())
    
    if n == 0 :
        break
    nums = [-1]+list(map(int, input().split()))
    depth, idx = -1, 0
    parent = [-1]*(n+1)
    for i in range(1,n+1):
        if nums[i] == k :
            idx = i
        if nums[i] - nums[i-1] != 1 :
            depth += 1
        parent[i] = depth
        
    result = 0
    target = parent[parent[idx]]
    for i in range(1,n+1):
        if parent[i] != parent[idx] and parent[parent[i]] == target:
            result += 1
            
    print(result)
    #print(parent)   