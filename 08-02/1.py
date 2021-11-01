#https://www.acmicpc.net/problem/1181
#백준 1181번 단어 정렬(정렬)
#import sys
#input = sys.stdin.readline

n = int(input())
words = set([input().rstrip() for _ in range(n)])

result = sorted(words, key = lambda x : (len(x),x))

for i in result:
    print(i)