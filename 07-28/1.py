#https://www.acmicpc.net/problem/14425
#백준 14425번 문자열 집합(문자열)
#import sys
#input = sys.stdin.readline

n, m = map(int, input().split())
keys = dict()

for i in range(n):
    word = input().rstrip()
    keys[word] = 1

result = 0

for _ in range(m):
    word = input().rstrip()
    if word in keys:
        result += 1
        
print(result)