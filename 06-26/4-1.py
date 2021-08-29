#https://www.acmicpc.net/problem/16437
#백준 16437번 양 구출 작전(dfs)
import sys
#input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def check(node):
    amount = graph[node][0]
    for bridge in graph[node][1]:
        amount += check(bridge)
        
    if amount > 0:
        return amount
    else:
        return 0

n = int(input())

graph = [[0,[]] for _ in range(n+1)]

for i in range(n-1):
    species, amount, bridge = input().split()
    if species == 'S':
        graph[i+2][0] = int(amount)
    else:
        graph[i+2][0] = -int(amount)
    graph[int(bridge)][1].append(i+2)
    
print(check(1))
'''
빠르게 처리하려면 DFS를 사용해서 재귀적으로 답을 구하지 않고 위상정렬을 활용하면 된다.
'''