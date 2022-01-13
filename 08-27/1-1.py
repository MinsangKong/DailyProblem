#https://www.acmicpc.net/problem/2503
#백준 2503번 숫자 야구 (순열)
#import sys
#input = sys.stdin.readline
from itertools import permutations

n = int(input())
nums = []
for _ in range(n):
    a,b,c = input().split()
    nums.append([list(map(int, a)),int(b),int(c)])
result = 0
base = [i for i in range(1,10)]

for num in permutations(base,3):
    flag = True
    for i in range(n):
        target, st, ball = nums[i]
        a,b = 0, 0
        for j in range(3):
            if num[j] == target[j]:
                a += 1
            elif target[j] in num :
                b += 1
        if st != a or ball != b :
            flag = False
            break
    if flag :
        #print(num)
        result += 1

print(result)