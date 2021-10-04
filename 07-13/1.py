#https://www.acmicpc.net/problem/11656
#백준 11656번 접미사 배열(문자열)
#import sys
#input = sys.stdin.readline

word = input().rstrip()

result = []

for i in range(len(word)):
    result.append(word[i:])
    
for i in sorted(result):
    print(i)