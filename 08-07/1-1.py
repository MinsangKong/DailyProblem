#https://www.acmicpc.net/problem/14594
#백준 14594번 동방 프로젝트 (유니온 파인드)
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
    else:
        parent[b] = a

n = int(input())
m = int(input())
rooms = [i for i in range(n+1)]
count = set()
result = n

if m :
    for i in range(m):
        a, b = map(int, input().split())
        count.add((a,b))
    for a,b in count:
        for i in range(a+1,b+1):
            if find_parent(rooms, a) != find_parent(rooms,i):
                union_parent(rooms,a,i)
                result -= 1

print(result)