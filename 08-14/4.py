#https://www.acmicpc.net/problem/18116
#백준 18116번 로봇 조립 (유니온 파인드)
#import sys
#input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b :
        parent[a] = b
        count[b] += count[a]
    else:
        parent[b] = a
        count[a] += count[b]

n = int(input())
count = [1]*(10**6+1)
parent = [i for i in range(10**6+1)]

for i in range(n):
    data = input().split()
    if data[0] == 'I':
        a, b = int(data[1]), int(data[2])
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent,a,b)
    else:
        print(count[find_parent(parent, int(data[1]))])