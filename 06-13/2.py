#https://www.acmicpc.net/problem/14400
#백준 14400번 편의점 2(정렬,그리디)
#import sys
#input = sys.stdin.readline

n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))
    
avgX = sorted(graph, key = lambda x: x[0])[n//2][0]
avgY = sorted(graph, key = lambda x: x[1])[n//2][1]


total = 0

for a,b in graph:
    total+= abs(a-avgX)+abs(b-avgY)
    
print(total)
'''
전체 값을 더하여 평균으로 낸 값보다 전체 배열의 중간에 위치한 값을 기준으로 한 경우가
더 작았다.
'''