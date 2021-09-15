#https://www.acmicpc.net/problem/1259
#백준 1259번 팰린드롬수(문자열)
#import sys
#input = sys.stdin.readline

while True:
    num = input().rstrip()
    if num == '0':
        break
    if num == num[::-1]:
        print('yes')
    else:
        print('no')