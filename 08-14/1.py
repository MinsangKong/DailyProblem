#https://www.acmicpc.net/problem/10546
#백준 10546번 배부른 마라토너(딕셔너리)
#import sys
#input = sys.stdin.readline

n = int(input())
count = dict()

for _ in range(n):
    name = input().rstrip()
    if name in count:
        count[name] += 1
    else:
        count[name] = 1
        
for _ in range(n-1):
    name = input().rstrip()
    count[name] -= 1
    
for name in count:
    if count[name]%2 == 1 :
        print(name)
        break