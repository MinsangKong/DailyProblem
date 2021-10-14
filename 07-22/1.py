#https://www.acmicpc.net/problem/6996
#백준 6996번 애너그램 (문자열)
import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    a,b = input().split()
    if sorted(a) == sorted(b):
        print("{} & {} are anagrams.".format(a,b))
    else:
        print("{} & {} are NOT anagrams.".format(a,b))