#https://www.acmicpc.net/problem/19637
#IF문 좀 대신 써줘 (이분탐색)
#import sys
#input = sys.stdin.readline

def find(target):
    s = 0
    e = len(case)
    while s < e :
        mid = (s+e)//2
        
        if case[mid] < target :
            s = mid + 1
        else:
            e = mid
    return e

n, m = map(int, input().split())
honor = dict()

for _ in range(n):
    a, b = input().split()
    if int(b) not in honor:
        honor[int(b)] = a
    
case = sorted(honor.keys())
    
for _ in range(m):
    num = int(input())
    idx = find(num)
    print(honor[case[idx]])