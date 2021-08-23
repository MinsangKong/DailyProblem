#https://www.acmicpc.net/problem/2250
#백준 2250번 트리의 높이와 너비(트리, 중위순회, BFS)
#import sys
#input = sys.stdin.readline
from collections import deque

def inorder(node, level):
    global depth
    if graph[node][0] != -1:
        inorder(graph[node][0], level+1)
    distance[level].append(depth)
    depth += 1
    if graph[node][1] != -1:
        inorder(graph[node][1], level+1)

n = int(input())
graph = [[] for _ in range(n+1)]
parent = [0] *(n+1)
distance = [[] for _ in range(n+1)]
root = 0

for _ in range(n):
    p, l, r = map(int, input().split())
    graph[p].append(l)
    graph[p].append(r)
    parent[p] += 1
    if l != -1:
        parent[l] +=1
    if r != -1:
        parent[r] +=1
    
for i in range(1,n+1):
    if parent[i] == 1:
        root = i
        break
        
depth = 1

inorder(root,1)
result = max(distance[1])-min(distance[1])+1
level = 1

for i in range(2,n+1):
    if distance[i]:
        if result < max(distance[i])-min(distance[i])+1:
            result = max(distance[i])-min(distance[i])+1
            level = i
            
print(level)
print(result)
'''
https://vixxcode.tistory.com/39 참고
트리 알고리즘을 따로 공부해야 할 것 같다...
'''