#https://www.acmicpc.net/problem/12893
#백준 12893번 적의적(MST)
#import sys
#input = sys.stdin.readline

import sys
input = sys.stdin.readline

n, m = map(int,input().split())

parent = [-1 for _ in range(n + 1)]
enemy = [0] * (n + 1)

def union(a, b) :
    a = find(a)
    b = find(b)

    if a != b :
        parent[b] = a
    
def find(x) :
    if parent[x] < 0 :
        return x

    else :
        parent[x] = find(parent[x])
        return parent[x]


answer = 1
for _ in range(m) :
    a, b = map(int,input().split()) # 서로 적

    a = find(a)
    b = find(b)

    if a == b : # 적끼리 같은 그룹이면 이론 성립 X
        answer = 0
        break

    a_enemy = enemy[a]
    b_enemy = enemy[b]

    # a의 적과 b를 동지로 설정한다.
    if a_enemy :
        union(a_enemy, b)
    else :
        enemy[a] = b # a의 적은 b이므로 
    

    # b의 적과 a를 동지로 설정
    if b_enemy : 
        union(b_enemy, a)
    else :
        enemy[b] = a
        

print(answer)
'''
find_parent와 union_parent를 활용하면 더 빠르게 풀 수 있었다.
'''