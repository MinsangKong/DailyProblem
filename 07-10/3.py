#https://www.acmicpc.net/problem/13164
#백준 1316번 행복 유치원(누적합, 그리디)
#import sys
#input = sys.stdin.readline

n, k = map(int, input().split())
heights = list(map(int, input().split()))

diff = [0]*(n-1)

for i in range(n-1):
    diff[i] = heights[i+1]-heights[i]
    
diff.sort()

print(sum(diff[:n-k]))