#https://www.acmicpc.net/problem/1343
#백준 1343번 폴리오미노(문자열)
#import sys
#input = sys.stdin.readline

word = input().rstrip()

word = word.replace('XXXX','AAAA').replace('XX', 'BB')

if 'X' in word:
    print(-1)
else:
    print(word)