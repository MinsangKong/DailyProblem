#https://www.acmicpc.net/problem/1620
#백준 1620번 나는야 포켓몬 마스터 이다솜 (딕셔너리)
#import sys
#input = sys.stdin.readline

n, m = map(int, input().split())

names = dict()
nums = dict()

for i in range(n):
    name = input().rstrip()
    names[name] = i+1
    nums[i+1] = name

for _ in range(m):
    key = input().rstrip()
    if key.isdigit():
        print(nums[int(key)])
    else:
        print(names[key])