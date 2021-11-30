#https://www.acmicpc.net/problem/20115
#백준 20115번 에너지 드링크 (정렬, 그리디)
#import sys
#input = sys.stdin.readline

n = int(input())
drinks = list(map(int, input().split()))
drinks.sort(reverse=True)

result = drinks[0]
for i in range(1,n):
    result += (drinks[i]/2)
if result == int(result):
    print(int(result))
else:
    print(result)