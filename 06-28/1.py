#https://www.acmicpc.net/problem/16171
#백준 16171번 나는 친구가 적다(그리디, 문자열)
#import sys
#input = sys.stdin.readline

word = input().rstrip()
key = input().rstrip()

wordMod = ''.join([i for i in word if not i.isdigit()])

if key in wordMod:
    print(1)
else:
    print(0)