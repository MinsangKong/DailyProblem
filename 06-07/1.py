#https://www.acmicpc.net/problem/11365
#백준 11365번 !밀비 급일(그리디)
#import sys
#input = sys.stdin.readline

while True:
    word = input().rstrip()
    if word =='END':
        break
    print(word[::-1])