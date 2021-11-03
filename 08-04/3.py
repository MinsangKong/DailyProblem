#https://www.acmicpc.net/problem/7511
#백준 7511번 소셜 네트워킹 어플리케이션(유니온파인드)
#import sys
#input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b :
        parent[a] = b
    else:
        parent[b] = a

t = int(input())

for s in range(t):
    n = int(input())
    k = int(input())
    parent = [i for i in range(n)]    
    for _ in range(k):
        a,b = map(int, input().split())
        union_parent(parent, a, b)
    m = int(input())

    print("Scenario {}:".format(s+1))
    for _ in range(m):
        a,b = map(int, input().split())
        if find_parent(parent, a) == find_parent(parent, b):
            print(1)
        else:
            print(0)
    print()